cwlVersion: v1.2
class: Workflow
requirements:
 ScatterFeatureRequirement: {}
inputs:
 in_csv: File
 col_name: string
 k: int

outputs:
 metrics:
   type: File
   outputSource: gather/res

steps:
 load_data:
  run: load_data.cwl
  in:
    csv_file: in_csv
    column_name: col_name
  out: [data]

 generate_k:
  run: generate_k.cwl
  in:
   k: k
  out: [k_list]

 calc:
  in:
    dataset: load_data/data
    k: generate_k/k_list
  scatter: [k]
  run: calc.cwl
  out: [fold]

 gather:
  in:
   errs: calc/fold
  run: gather.cwl
  out: [res]