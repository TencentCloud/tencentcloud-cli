**Example 1: 错误示例**

人员性别设置错误

Input: 

```
tccli iai ModifyPersonBaseInfo --cli-unfold-argument  \
    --PersonId 1001 \
    --Gender -1 \
    --Version 2018-03-01
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.PersonGenderIllegal",
            "Message": "人员性别设置出错。0代表未填写，1代表男性，2代表女性。"
        },
        "RequestId": "f40bf659-0283-4773-abe8-945f643d5015"
    }
}
```

**Example 2: 修改人员基础信息接口**



Input: 

```
tccli iai ModifyPersonBaseInfo --cli-unfold-argument  \
    --PersonId 2001 \
    --PersonName JunlyWang \
    --Gender 1 \
    --Version 2018-03-01
```

Output: 
```
{
    "Response": {
        "RequestId": "6e2a0fb7-7c9e-45c7-abf1-338457d1def7"
    }
}
```

**Example 3: 修改人员基础信息接口-2**



Input: 

```
tccli iai ModifyPersonBaseInfo --cli-unfold-argument  \
    --PersonId 1001 \
    --PersonName EvanLiao \
    --Gender 1 \
    --Version 2018-03-01
```

Output: 
```
{
    "Response": {
        "RequestId": "6e2a0fb7-7c9e-45c7-abf1-338457d1def7"
    }
}
```

