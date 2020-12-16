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
patient_health <- dbReadTable(con, "PatientHealth")


# Alle Werte eines bestimmten Patienten jeweils für einen Gesundheitsparameter

all_vals_for_patient_health_param <- function(patient_name, param_description) {
  
  patient_id <- patient[patient[, "last_name"] == patient_name,]$patient_nr
  
  patient_health_ids <- patient_health[patient_health[, "patientnr"] == patient_id,]$healthvalue
  
  health_parameter_id <- health_parameter[health_parameter[, "denotation"] == param_description,]$hpid
  
  health_values_by_parameter <- health_value[health_value[, "parameter"] == health_parameter_id,]
  
  health_values_by_parameter_and_patient <- health_values_by_parameter[health_values_by_parameter$gid %in% patient_health_ids ,]
  
  return(health_values_by_parameter_and_patient$value)
}

# Durchschnitt über die Werte eines Patienten pro Gesundheitsparameter

average_for_each_health_param_per_patient <- function(patient_name) {
  
  health_params <- health_parameter$denotation

  health_params_avg <- c()
  
  for(param in health_params) {
    
    vals <- all_vals_for_patient_health_param(patient_name=patient_name, param_description=param)
    
    health_params_avg <- c(health_params_avg, mean(vals))
  }
  
  return(health_params_avg)
}


res = all_vals_for_patient_health_param(patient_name="Frey", 
                                        param_description="Plebismus")
print(res)


res = average_for_each_health_param_per_patient(patient_name="Frey")
print(res)


