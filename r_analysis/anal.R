#library(RPostgres)
#library(rlist)

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


# Alle Werte eines bestimmten Patienten jeweils für einen Gesundheitsparameter
HealthParameterID <- 1
PantientID <- 1
sql <- paste('SELECT first_name, last_name, denotation, value 
              FROM "Patient"
              INNER JOIN "patient_health" ON "Patient".id="patient_health".patient_id
              INNER JOIN "HealthValue" ON "patient_health".healthvalue_id="HealthValue".id
              INNER JOIN "HealthParameter" ON "HealthValue".parameter="HealthParameter".id
              WHERE "HealthParameter".id=', HealthParameterID, 'AND "Patient".id=', PantientID) 

query <- dbGetQuery(con, sql)
print(query)

# Durchschnitt über die Werte eines Patienten pro Gesundheitsparameter
PantientID <- 1
sql <- paste('SELECT denotation, AVG(value) 
              FROM "Patient"
              INNER JOIN "patient_health" ON "Patient".id="patient_health".patient_id
              INNER JOIN "HealthValue" ON "patient_health".healthvalue_id="HealthValue".id
              INNER JOIN "HealthParameter" ON "HealthValue".parameter="HealthParameter".id
              WHERE "Patient".id=', PantientID, 'Group by denotation') 

query <- dbGetQuery(con, sql)
print(query)