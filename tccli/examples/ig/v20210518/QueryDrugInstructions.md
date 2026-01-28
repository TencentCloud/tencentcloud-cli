**Example 1: 药品查询**



Input: 

```
tccli ig QueryDrugInstructions --cli-unfold-argument  \
    --PartnerId 1*******4 \
    --PartnerSecret **************a36bbdd17960b3d70e \
    --HospitalAppId ******38323 \
    --Message 阿莫西林分散片
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": [
            {
                "DrugInfos": [
                    {
                        "AdverseReaction": "",
                        "DocUrl": "https://dev-guidetaro.wecity.qq.com/guide-*lm/drugDetail?drugHashId=00*45c1ca6695ca2d4679f60a4f4cea929390eb3&channel=llmApi&appid=ky800038323&configure=drug",
                        "DrugId": "00045c1ca*695c*2d4679f60a4f4cea929390eb3",
                        "DrugName": "阿莫西林分散片",
                        "DrugRxType": 1,
                        "DrugUsage": "",
                        "Indication": "",
                        "Manufacturer": "石药集团中诺药业(石家庄)有限公司",
                        "Specification": "500mg*6片",
                        "TradeName": ""
                    }
                ],
                "StandardDrugName": "药品信息"
            }
        ],
        "Message": "success",
        "RequestId": "2fb04389-9d51-4f67-a57d-362b03d57963"
    }
}
```

