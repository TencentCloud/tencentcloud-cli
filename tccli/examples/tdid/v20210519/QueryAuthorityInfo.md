**Example 1: 查询权威机构信息**

查询权威机构信息

Input: 

```
tccli tdid QueryAuthorityInfo --cli-unfold-argument  \
    --Did did:tdid:w1:0xbbf1dee9e082e1a54dd3973beedc59ff7e452862 \
    --DAPId 5 \
    --Name 某教育学院
```

Output: 
```
{
    "Response": {
        "RequestId": "3d5e7818-5027-44ca-bb03-68a9d5389bca",
        "Did": "did:tdid:w1:0xbbf1dee9e082e1a54dd3973beedc59ff7e452862",
        "Name": "某教育学院",
        "Status": 1,
        "Description": "职业教育",
        "RecognizeTime": "2023-09-19 11:54:25"
    }
}
```

