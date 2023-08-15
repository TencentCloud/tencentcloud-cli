**Example 1: 获取人员归属信息接口**



Input: 

```
tccli iai GetPersonGroupInfo --cli-unfold-argument  \
    --PersonId 2001 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "GroupNum": "1",
        "PersonGroupInfos": [
            {
                "GroupId": "ZhuYuanDormitoryNo1",
                "PersonExDescriptions": [
                    "计算机学院",
                    "软件工程",
                    "15级",
                    "3150108080"
                ]
            }
        ],
        "FaceModelVersion": "3.0",
        "RequestId": "671f0a1d-2b35-47c4-b9d1-b18053f71a04"
    }
}
```

**Example 2: 获取人员归属信息接口-2**



Input: 

```
tccli iai GetPersonGroupInfo --cli-unfold-argument  \
    --PersonId 1001 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "GroupNum": "1",
        "PersonGroupInfos": [
            {
                "GroupId": "TencentShenZhenEmployee",
                "PersonExDescriptions": [
                    "云与智慧产业事业群",
                    "大数据及人工智能产品中心",
                    "人脸识别产品组"
                ]
            }
        ],
        "FaceModelVersion": "3.0",
        "RequestId": "b7a505ad-4a85-42da-97b3-886c7999fb76"
    }
}
```

**Example 3: 错误示例**

人员ID不存在

Input: 

```
tccli iai GetPersonGroupInfo --cli-unfold-argument  \
    --PersonId 1002 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.PersonIdNotExist",
            "Message": "人员ID不存在。"
        },
        "RequestId": "98330f25-eb2e-432a-a30c-3830774210c1"
    }
}
```

