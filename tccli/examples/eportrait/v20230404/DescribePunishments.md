**Example 1: DescribePunishments1**

DescribePunishments1

Input: 

```
tccli eportrait DescribePunishments --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Eid 0001686fc131a4b3bbf0d429ee46e191
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "BasedOn": null,
                "Content": "吊销执照（登记证）",
                "Date": "2018-06-29",
                "Department": "沭阳县市场监督管理局",
                "IllegalType": null,
                "Number": "沭市监案（2018）第00702号",
                "Reason": null
            }
        ],
        "RequestId": "c461a60d-0d37-4863-9a23-62106f152398",
        "TotalCount": 1
    }
}
```

