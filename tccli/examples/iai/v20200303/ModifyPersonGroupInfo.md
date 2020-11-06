**Example 1: Modifying person description**



Input: 

```
tccli iai ModifyPersonGroupInfo --cli-unfold-argument  \
    --GroupId ZhuYuanDormitoryNo1 \
    --PersonId 2001 \
    --PersonExDescriptionInfos.0.PersonExDescriptionIndex 3 \
    --PersonExDescriptionInfos.0.PersonExDescription 3150108080
```

Output: 
```
{
    "Response": {
        "RequestId": "77e11a2d-0fc0-4fba-ab25-016e998221c3"
    }
}
```

**Example 2: Modifying person description - 2**



Input: 

```
tccli iai ModifyPersonGroupInfo --cli-unfold-argument  \
    --GroupId TencentShenZhenEmployee \
    --PersonId 1001 \
    --PersonExDescriptionInfos.0.PersonExDescriptionIndex 1 \
    --PersonExDescriptionInfos.0.PersonExDescription 'Big Data and AI Product Center'
```

Output: 
```
{
    "Response": {
        "RequestId": "77e11a2d-0fc0-4fba-ab25-016e998221c3"
    }
}
```

**Example 3: Sample error**

Invalid subscript.

Input: 

```
tccli iai ModifyPersonGroupInfo --cli-unfold-argument  \
    --GroupId TencentShenZhenEmployee \
    --PersonId 1001 \
    --PersonExDescriptionInfos.0.PersonExDescriptionIndex -1 \
    --PersonExDescriptionInfos.0.PersonExDescription 'AI Lab'
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "The value type of parameter `PersonExDescriptionInfos.0.PersonExDescriptionIndex` is not valid."
        },
        "RequestId": "f944657d-6260-4a2e-a4d8-9c1845f39e56"
    }
}
```

