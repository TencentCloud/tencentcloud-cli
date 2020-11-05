**Example 1: Face comparison for silent liveness detection**



Input: 

```
tccli faceid LivenessCompare --cli-unfold-argument  \
    --ImageBase64 <ImageBase64>\
    --VideoBase64 <VideoBase64>\
    --LivenessType SILENT
```

Output: 
```
{
    "Response": {
        "Result": "Success",
        "Description": "Success",
        "BestFrameBase64": "Imagebase64",
        "Sim": "89.88",
        "RequestId": "f904f4cf-75db-4f8f-a5ec-dc4f942c7f7a"
    }
}
```

