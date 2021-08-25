
from cohortextractor import (
  StudyDefinition,
  patients,
  codelist_from_csv,
  codelist,
  filter_codes_by_category,
  combine_codelists,
)

# Import codelists.py script
import codelists

# import json module
import json

# import study dates
# change this in design.R if necessary
with open("./analysis/lib/dates.json") as f:
  studydates = json.load(f)

# define variables explicitly
start_date = studydates["start_date"] 
start_date_pfizer = studydates["start_date_pfizer"] 
start_date_az = studydates["start_date_az"] 
start_date_moderna = studydates["start_date_moderna"]
end_date = studydates["end_date"]


## function to add days to a string date
from datetime import datetime, timedelta
def days(datestring, days):
  
  dt = datetime.strptime(datestring, "%Y-%m-%d").date()
  dt_add = dt + timedelta(days)
  datestring_add = datetime.strftime(dt_add, "%Y-%m-%d")

  return datestring_add



## function for diagnosis-specific A&E attendances
with open("./analysis/lib/diagnosis_groups.json") as f:
  diagnosis_groups = json.load(f)

def emergency_bydiagnosis_date(codelist_dict, on_date):
  """
  creates a new variable for each emergency attendance diagnosis
  """
  def make_variable(diagnosis_codelist, name, on_date):
    return {
      f"emergency_{name}_date": (
        patients.attended_emergency_care(
          returning="date_arrived",
          between=[on_date, on_date],
          date_format="YYYY-MM-DD",
          with_these_diagnoses = codelist(diagnosis_codelist, system="snomed"),
          return_expectations={
            "date": {"earliest": "2021-05-01", "latest" : "2021-06-01"},
            "rate": "uniform",
            "incidence": 0.05,
          },
        )
      )
  }

  variables = {}
  for name in codelist_dict.keys():
    diagnosis_codelist = codelist_dict[name]
    variables.update(make_variable(diagnosis_codelist, name, on_date))
  return variables





# start_date is currently set to the start of the vaccination campaign
# end_date depends on the most reent data coverage in the database, and the particular variables of interest

# Specifiy study defeinition
study = StudyDefinition(
  # Configure the expectations framework
  default_expectations={
    "date": {"earliest": "1970-01-01", "latest": end_date},
    "rate": "uniform",
    "incidence": 0.2,
  },
  
  index_date = start_date,
  # This line defines the study population
  population=patients.satisfying(
    """
        registered
        AND
        (age >= 18 AND age < 120)
        AND
        NOT died
        AND 
        covid_vax_any_1_date
        """,
    registered=patients.registered_as_of(
      "covid_vax_any_1_date - 1 days",
    ),
    died=patients.died_from_any_cause(
      on_or_before="covid_vax_any_1_date - 1 days",
      returning="binary_flag",
    ),
  ),
  
  
  ###############################################################################
  # COVID VACCINATION
  ###############################################################################
  
  #################################################################
  ## COVID VACCINATION TYPE = pfizer
  #################################################################
  
  covid_vax_pfizer_1_date=patients.with_tpp_vaccination_record(
    product_name_matches="COVID-19 mRNA Vaccine Pfizer-BioNTech BNT162b2 30micrograms/0.3ml dose conc for susp for inj MDV",
    find_first_match_in_period=True,
    returning="date",
    date_format="YYYY-MM-DD",
    return_expectations={
      "date": {
        "earliest": start_date_pfizer,  
        "latest": days(start_date_pfizer, 120),
      },
      "incidence": 0.001
    },
  ),
  
  
  covid_vax_pfizer_2_date=patients.with_tpp_vaccination_record(
    product_name_matches="COVID-19 mRNA Vaccine Pfizer-BioNTech BNT162b2 30micrograms/0.3ml dose conc for susp for inj MDV",
    on_or_after="covid_vax_pfizer_1_date + 1 days",
    find_first_match_in_period=True,
    returning="date",
    date_format="YYYY-MM-DD",
    return_expectations={
      "date": {
        "earliest": start_date_pfizer,  
        "latest": days(start_date_pfizer, 120),
      },
      "incidence": 1
    },
  ),
  
  covid_vax_pfizer_3_date=patients.with_tpp_vaccination_record(
    product_name_matches="COVID-19 mRNA Vaccine Pfizer-BioNTech BNT162b2 30micrograms/0.3ml dose conc for susp for inj MDV",
    on_or_after="covid_vax_pfizer_2_date + 1 days",
    find_first_match_in_period=True,
    returning="date",
    date_format="YYYY-MM-DD",
    return_expectations={
      "date": {
        "earliest": "2020-12-29",  # first reported second dose administered on the 29/12
        "latest": "2021-02-01",
      },
      "incidence": 0.2
    },
  ),
  
  
  #################################################################
  ## COVID VACCINATION TYPE = Oxford -AZ
  #################################################################
  
  covid_vax_az_1_date=patients.with_tpp_vaccination_record(
    product_name_matches="COVID-19 Vac AstraZeneca (ChAdOx1 S recomb) 5x10000000000 viral particles/0.5ml dose sol for inj MDV",
    find_first_match_in_period=True,
    returning="date",
    date_format="YYYY-MM-DD",
    return_expectations={
      "date": {
        "earliest": start_date_az, 
        "latest": days(start_date_az, 120),
      },
      "incidence": 0.001
    },
  ),
  
  
  covid_vax_az_2_date=patients.with_tpp_vaccination_record(
    product_name_matches="COVID-19 Vac AstraZeneca (ChAdOx1 S recomb) 5x10000000000 viral particles/0.5ml dose sol for inj MDV",
    on_or_after="covid_vax_az_1_date + 1 days",
    find_first_match_in_period=True,
    returning="date",
    date_format="YYYY-MM-DD",
    return_expectations={
      "date": {
        "earliest": start_date_az,  
        "latest": days(start_date_az, 120),
      },
      "incidence": 1
    },
  ),
  
  covid_vax_az_3_date=patients.with_tpp_vaccination_record(
    product_name_matches="COVID-19 Vac AstraZeneca (ChAdOx1 S recomb) 5x10000000000 viral particles/0.5ml dose sol for inj MDV",
    on_or_after="covid_vax_az_2_date + 1 days",
    find_first_match_in_period=True,
    returning="date",
    date_format="YYYY-MM-DD",
    return_expectations={
      "date": {
        "earliest": "2021-02-01",
        "latest": "2021-03-01",
        "incidence": 0.3
      }
    },
  ),
  
  
  #################################################################
  ## COVID VACCINATION TYPE = moderna
  #################################################################
  covid_vax_moderna_1_date=patients.with_tpp_vaccination_record(
    product_name_matches="COVID-19 mRNA (nucleoside modified) Vaccine Moderna 0.1mg/0.5mL dose dispersion for inj MDV",
    find_first_match_in_period=True,
    returning="date",
    date_format="YYYY-MM-DD",
    return_expectations={
      "date": {
        "earliest": start_date_moderna, 
        "latest": days(start_date_moderna, 120),
      },
      "incidence": 0.001
    },
  ),
  
  
  covid_vax_moderna_2_date=patients.with_tpp_vaccination_record(
    product_name_matches="COVID-19 mRNA (nucleoside modified) Vaccine Moderna 0.1mg/0.5mL dose dispersion for inj MDV",
    on_or_after="covid_vax_moderna_1_date + 1 days",
    find_first_match_in_period=True,
    returning="date",
    date_format="YYYY-MM-DD",
    return_expectations={
      "date": {
        "earliest": start_date_moderna, 
        "latest": days(start_date_moderna, 120),
      },
      "incidence": 1
    },
  ),
  
  covid_vax_moderna_3_date=patients.with_tpp_vaccination_record(
    product_name_matches="COVID-19 mRNA (nucleoside modified) Vaccine Moderna 0.1mg/0.5mL dose dispersion for inj MDV",
    on_or_after="covid_vax_moderna_2_date + 1 days",
    find_first_match_in_period=True,
    returning="date",
    date_format="YYYY-MM-DD",
    return_expectations={
      "date": {
        "earliest": "2021-02-01",
        "latest": "2021-03-01",
        "incidence": 0.3
      }
    },
  ),
  
  
  #################################################################
  ## COVID VACCINATION TYPE = any based on disease target
  #################################################################
  
  # any prior covid vaccination
  covid_vax_disease_1_date=patients.with_tpp_vaccination_record(
    target_disease_matches="SARS-2 CORONAVIRUS",
    find_first_match_in_period=True,
    returning="date",
    date_format="YYYY-MM-DD",
    return_expectations={
      "date": {
        "earliest": start_date, 
        "latest": days(start_date, 120),
      },
      "incidence": 0.001
    },
  ),
  
  covid_vax_disease_2_date=patients.with_tpp_vaccination_record(
    target_disease_matches="SARS-2 CORONAVIRUS",
    on_or_after="covid_vax_disease_1_date + 1 days",
    find_first_match_in_period=True,
    returning="date",
    date_format="YYYY-MM-DD",
    return_expectations={
      "date": {
        "earliest": start_date, 
        "latest": days(start_date, 120),
      },
      "incidence": 1
    },
  ),
  # SECOND DOSE COVID VACCINATION - any type
  covid_vax_disease_3_date=patients.with_tpp_vaccination_record(
    target_disease_matches="SARS-2 CORONAVIRUS",
    on_or_after="covid_vax_disease_2_date + 1 days",
    find_first_match_in_period=True,
    returning="date",
    date_format="YYYY-MM-DD",
    return_expectations={
      "date": {
        "earliest": "2021-02-02",
        "latest": "2021-04-30",
      }
    },
  ),
  
  #################################################################
  ## COVID VACCINATION TYPE = combine brands
  #################################################################
  # any COVID vaccination, combination of az and pfizer
  
  covid_vax_any_1_date=patients.minimum_of(
    "covid_vax_pfizer_1_date", "covid_vax_az_1_date", "covid_vax_moderna_1_date"
  ),
  
  covid_vax_any_2_date=patients.minimum_of(
    "covid_vax_pfizer_2_date", "covid_vax_az_2_date", "covid_vax_moderna_2_date"
  ),
  
  covid_vax_any_3_date=patients.minimum_of(
    "covid_vax_pfizer_3_date", "covid_vax_az_3_date", "covid_vax_moderna_3_date"
  ),
  



  ################################################
  ###### PRACTICE AND PATIENT ADDRESS VARIABLES ##
  ################################################
  
  
  # practice pseudo id
  practice_id=patients.registered_practice_as_of(
    "covid_vax_any_1_date - 1 days",
    returning="pseudo_id",
    return_expectations={
      "int": {"distribution": "normal", "mean": 1000, "stddev": 100},
      "incidence": 1,
    },
  ),
  
  # msoa=patients.address_as_of(
  #   "covid_vax_any_1_date - 1 days",
  #   returning="msoa",
  #   return_expectations={
  #     "rate": "universal",
  #     "category": {"ratios": {"E02000001": 0.0625, "E02000002": 0.0625, "E02000003": 0.0625, "E02000004": 0.0625,
  #       "E02000005": 0.0625, "E02000007": 0.0625, "E02000008": 0.0625, "E02000009": 0.0625, 
  #       "E02000010": 0.0625, "E02000011": 0.0625, "E02000012": 0.0625, "E02000013": 0.0625, 
  #       "E02000014": 0.0625, "E02000015": 0.0625, "E02000016": 0.0625, "E02000017": 0.0625}},
  #   },
  # ),  
  
  # stp is an NHS administration region based on geography
  stp=patients.registered_practice_as_of(
    "covid_vax_any_1_date - 1 days",
    returning="stp_code",
    return_expectations={
      "rate": "universal",
      "category": {
        "ratios": {
          "STP1": 0.1,
          "STP2": 0.1,
          "STP3": 0.1,
          "STP4": 0.1,
          "STP5": 0.1,
          "STP6": 0.1,
          "STP7": 0.1,
          "STP8": 0.1,
          "STP9": 0.1,
          "STP10": 0.1,
        }
      },
    },
  ),
  
  # NHS administrative region
  region=patients.registered_practice_as_of(
    "covid_vax_any_1_date - 1 days",
    returning="nuts1_region_name",
    return_expectations={
      "rate": "universal",
      "category": {
        "ratios": {
          "North East": 0.1,
          "North West": 0.1,
          "Yorkshire and The Humber": 0.2,
          "East Midlands": 0.1,
          "West Midlands": 0.1,
          "East": 0.1,
          "London": 0.1,
          "South East": 0.1,
          "South West": 0.1
          #"" : 0.01
        },
      },
    },
  ),
  
  
  ## IMD - quintile
  
  imd=patients.address_as_of(
    "covid_vax_any_1_date - 1 days",
    returning="index_of_multiple_deprivation",
    round_to_nearest=100,
    return_expectations={
      "category": {"ratios": {c: 1/320 for c in range(100, 32100, 100)}}
    }
  ),
  
  dereg_date=patients.date_deregistered_from_all_supported_practices(
    on_or_after="covid_vax_any_1_date",
    date_format="YYYY-MM-DD",
    return_expectations={
      "date": {
        "earliest": "2020-08-01",
        "latest": "2021-12-07",
      },
      "incidence": 0.001
    }
  ),
  


  ###############################################################################
  # DEMOGRAPHICS
  ###############################################################################
  
  
  
  # https://github.com/opensafely/risk-factors-research/issues/49
  age=patients.age_as_of( 
    "covid_vax_any_1_date - 1 days",
    return_expectations={
      "rate": "universal",
      "int": {"distribution": "population_ages"},
      "incidence" : 1
    },
  ),
  
  age_mar20=patients.age_as_of( 
    "2020-03-31",
    return_expectations={
      "rate": "universal",
      "int": {"distribution": "population_ages"},
      "incidence" : 1
    },
  ),
  
  # https://github.com/opensafely/risk-factors-research/issues/46
  sex=patients.sex(
    return_expectations={
      "rate": "universal",
      "category": {"ratios": {"M": 0.49, "F": 0.51}},
      "incidence": 1,
    }
  ),
  
  
  # ETHNICITY IN 6 CATEGORIES
  ethnicity = patients.with_these_clinical_events(
    codelists.ethnicity,
    returning="category",
    find_last_match_in_period=True,
    include_date_of_match=False,
    return_expectations={
      "category": {"ratios": {"1": 0.2, "2": 0.2, "3": 0.2, "4": 0.2, "5": 0.2}},
      "incidence": 0.75,
    },
  ),
  
  # ethnicity variable that takes data from SUS
  ethnicity_6_sus = patients.with_ethnicity_from_sus(
    returning="group_6",  
    use_most_frequent_code=True,
    return_expectations={
      "category": {"ratios": {"1": 0.2, "2": 0.2, "3": 0.2, "4": 0.2, "5": 0.2}},
      "incidence": 0.8,
    },
  ),
  
  hscworker = patients.with_healthcare_worker_flag_on_covid_vaccine_record(returning="binary_flag"),
  
  
  care_home_type=patients.care_home_status_as_of(
      "index_date - 1 day",
      categorised_as={
          "Carehome": """
            IsPotentialCareHome
            AND LocationDoesNotRequireNursing='Y'
            AND LocationRequiresNursing='N'
          """,
          "Nursinghome": """
            IsPotentialCareHome
            AND LocationDoesNotRequireNursing='N'
            AND LocationRequiresNursing='Y'
          """,
          "Mixed": "IsPotentialCareHome",
          "": "DEFAULT",  # use empty string
      },
      return_expectations={
          "category": {"ratios": {"Carehome": 0.05, "Nursinghome": 0.05, "Mixed": 0.05, "": 0.85, }, },
          "incidence": 1,
      },
  ),

  # simple care home flag
  care_home_tpp=patients.satisfying(
      """care_home_type""",
      return_expectations={"incidence": 0.01},
  ),
  
  care_home_code=patients.with_these_clinical_events(
      codelists.carehome,
      on_or_before="index_date - 1 day",
      returning="binary_flag",
      return_expectations={"incidence": 0.01},
  ),
  
  
  ################################################
  ############ post-vaccination events    ########
  ################################################
  
  
  # any emergency attendance
  emergency_date=patients.attended_emergency_care(
    returning="date_arrived",
    on_or_after="covid_vax_any_1_date",
    date_format="YYYY-MM-DD",
    find_first_match_in_period=True,
    return_expectations={
      "date": {"earliest": "2021-05-01", "latest" : "2021-06-01"},
      "rate": "uniform",
      "incidence": 0.05,
    },
  ),
  
  # diagnosis specific A&E attendance
  **emergency_bydiagnosis_date(diagnosis_groups, on_date="emergency_date"),
  
  # Death
  death_date=patients.died_from_any_cause(
    returning="date_of_death",
    date_format="YYYY-MM-DD",
    return_expectations={
      "date": {"earliest": "2021-06-01", "latest" : "2021-08-01"},
      "rate": "uniform",
      "incidence": 0.02
    },
  ),

)
