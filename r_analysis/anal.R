#library(RPostgres)
#library(rlist)
#library(ggplot2)

con <- dbConnect(RPostgres::Postgres(), 
                 dbname = "patientdb", 
                 host="localhost", 
                 port=5432, 
                 user = 'postgres',
                 password="1234")  

health_parameter <- dbReadTable(con, "HealthParameter")
health_value <- dbReadTable(con, "HealthValue")
patient <- dbReadTable(con, "Patient")
patient_health <- dbReadTable(con, "patient_health")


vals_by_patient_and_health <- function(HealthParameterID, PantientID) {
  # Alle Werte eines bestimmten Patienten jeweils für einen Gesundheitsparameter
  sql <- paste('SELECT first_name, last_name, denotation, value 
                FROM "Patient"
                INNER JOIN "patient_health" ON "Patient".id="patient_health".patient_id
                INNER JOIN "HealthValue" ON "patient_health".healthvalue_id="HealthValue".id
                INNER JOIN "HealthParameter" ON "HealthValue".parameter="HealthParameter".id
                WHERE "HealthParameter".id=', HealthParameterID, 'AND "Patient".id=', PantientID) 
  
  query <- dbGetQuery(con, sql)
  print(query)
}

avg_vals_by_patient_and_health <- function(PantientID) {
  # Durchschnitt über die Werte eines Patienten pro Gesundheitsparameter
  sql <- paste('SELECT denotation, AVG(value) 
                FROM "Patient"
                INNER JOIN "patient_health" ON "Patient".id="patient_health".patient_id
                INNER JOIN "HealthValue" ON "patient_health".healthvalue_id="HealthValue".id
                INNER JOIN "HealthParameter" ON "HealthValue".parameter="HealthParameter".id
                WHERE "Patient".id=', PantientID, 'Group by denotation')
  
  query <- dbGetQuery(con, sql)
  print(query)
}

avg_health <- function() {
  # Durchschnitt über die Werte pro Gesundheitsparameters über alle Patienten
  sql <- paste('SELECT denotation, AVG(value) 
                FROM "Patient"
                INNER JOIN "patient_health" ON "Patient".id="patient_health".patient_id
                INNER JOIN "HealthValue" ON "patient_health".healthvalue_id="HealthValue".id
                INNER JOIN "HealthParameter" ON "HealthValue".parameter="HealthParameter".id
                Group by denotation') 
  
  query <- dbGetQuery(con, sql)
  print(query)
}

median_health <- function() {
  # Median der Werte pro Gesundheitsparameter über alle Patienten
  sql <- paste('SELECT denotation, value
                FROM "Patient"
                INNER JOIN "patient_health" ON "Patient".id="patient_health".patient_id
                INNER JOIN "HealthValue" ON "patient_health".healthvalue_id="HealthValue".id
                INNER JOIN "HealthParameter" ON "HealthValue".parameter="HealthParameter".id') 
  
  query <- dbGetQuery(con, sql)
  res = aggregate(query[, 2], list(query$denotation), median)
  print(res)
}

sd_health_byhealth <- function(HealthParameterID) {
# Standardabweichung der Werte eines bestimmten Gesundheitsparameters über alle Patienten
  sql <- paste('SELECT denotation, value
                FROM "Patient"
                INNER JOIN "patient_health" ON "Patient".id="patient_health".patient_id
                INNER JOIN "HealthValue" ON "patient_health".healthvalue_id="HealthValue".id
                INNER JOIN "HealthParameter" ON "HealthValue".parameter="HealthParameter".id
                WHERE "HealthParameter".id=', HealthParameterID)  
  
  query <- dbGetQuery(con, sql)
  res = aggregate(query[, 2], list(query$denotation), sd)
  # result includes bessel'S correction (n-1)
  print(res)
}

#TODO fix this (shows always the same)
plot_vals_by_patient_and_health <- function(HealthParameterID, PantientID) {
  # Zeichnen Sie geeignete Diagramme zur Visualisierung der Daten mit Hilfe von ggplot
  # Alle Parameter-Werte eines bestimmten Patienten zu einem bestimmten Parameter
  
  sql <- paste('SELECT value, "HealthParameter".denotation 
                FROM "Patient"
                INNER JOIN "patient_health" ON "Patient".id="patient_health".patient_id
                INNER JOIN "HealthValue" ON "patient_health".healthvalue_id="HealthValue".id
                INNER JOIN "HealthParameter" ON "HealthValue".parameter="HealthParameter".id
                WHERE "HealthParameter".id=', HealthParameterID, 'AND "Patient".id=', PantientID) 
  
  query <- dbGetQuery(con, sql)
  p <- ggplot(query, aes(x=rownames(query), y=query[,1])) + geom_bar(stat = "identity", width=0.2, color="blue",fill="aquamarine") + ggtitle(paste(query$denotation," Werte für Patient")) + xlab("Wert ID") + ylab("Wert")
  print(p)
}

#TODO fix this (shows always the same)
plot_avg_health_by_patient <- function(HealthParameterID) {
  # Durchschnitte der Parameterwerte über alle Patienten (also pro Patient Durchschnitt der Parameterwerte eines bestimmten Parameters)
  # peo patient durschnitt für werte
  
  sql <- paste('SELECT patient_id, AVG(value), "HealthParameter".denotation
                FROM "Patient"
                INNER JOIN "patient_health" ON "Patient".id="patient_health".patient_id
                INNER JOIN "HealthValue" ON "patient_health".healthvalue_id="HealthValue".id
                INNER JOIN "HealthParameter" ON "HealthValue".parameter="HealthParameter".id
                WHERE "HealthParameter".id=', HealthParameterID, 'Group by patient_id, denotation') 
  
  query <- dbGetQuery(con, sql)
  query <- dbGetQuery(con, sql)
  p <- ggplot(query, aes(x=query[,1], y=query[,2])) + geom_bar(stat = "identity", width=1, color="blue",fill="aquamarine") +  ggtitle(paste("Durchschnittliche",query$denotation,"Werte pro Patient")) + xlab("Patienten ID") + ylab("Wert im Durchscnitt")
  print(p)
}

