cwlVersion: v1.2
class: CommandLineTool
inputs:
 k: int
baseCommand: ["echo"]
outputs:
 k_list:
  type: int[]
  outputBinding:
   outputEval: |-
        ${
          var out = []
          for(var i = 1; i <= inputs.k; i++) {
            out.push(i)
          }
          return out
        }

requirements:
  InlineJavascriptRequirement: {}