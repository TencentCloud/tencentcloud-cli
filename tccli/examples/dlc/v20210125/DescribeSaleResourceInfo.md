**Example 1: DescribeSaleResourceInfo**



Input: 

```
tccli dlc DescribeSaleResourceInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "SaleResourceInfoList": [
            {
                "ResourceSpec": {
                    "ResourceType": "CPU",
                    "InstanceType": "",
                    "GpuType": "",
                    "BillingItem": "sv_dlc_standard_cu_standard_cu",
                    "SpecDesc": "1 CU = 1 × vCPU * 4GB Memory",
                    "Spec": "0:1:4:0",
                    "MaxCardPerNode": 0
                },
                "Step": 32,
                "MaxSpec": 4096,
                "StatusCategory": "EnoughStock"
            }
        ],
        "RequestId": "313630c6-9e14-44ae-b9d6-00f019357803"
    }
}
```

