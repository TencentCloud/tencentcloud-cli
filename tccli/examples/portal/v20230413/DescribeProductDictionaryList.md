**Example 1: 产品字典列表**

获取产品字典列表

Input: 

```
tccli portal DescribeProductDictionaryList --cli-unfold-argument  \
    --DictIds 2000 \
    --IncludeActivity True \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "DictId": 2000,
                "ParentId": 500,
                "Type": 1,
                "Slug": "cvm",
                "Name": "云服务器",
                "ProductOwner": [
                    "xxxxxxxxx"
                ],
                "DeveloperOwner": [
                    "xxxxxxxxx"
                ],
                "FtId": 100,
                "Weight": 2030050000,
                "IntroPageLink": "https://cloud.tencent.com/product/cvm",
                "IntroUpdateTime": "2023-07-03T09:53:44+08:00",
                "Acts": [
                    "https://cloud.tencent.com/act/pro/618season"
                ]
            }
        ],
        "RequestId": "f230e543-9187-4614-9dcf-9959458ac284",
        "Total": 1
    }
}
```

**Example 2: 产品字典信息**

产品字典信息

Input: 

```
tccli portal DescribeProductDictionaryList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --DictIds 2000
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Acts": null,
                "BelongL3Id": 0,
                "DeveloperOwner": [
                    "abelsu",
                    "aidanpeng",
                    "alanqianghe",
                    "alfieliu",
                    "andersonyli",
                    "arikxzheng",
                    "asinli",
                    "dannykong",
                    "diluczhang",
                    "dondonchen",
                    "eliqiao",
                    "erinpan",
                    "errrroryang",
                    "fengxxxu",
                    "fielixlv",
                    "gardennchen",
                    "hebessli",
                    "ianhu",
                    "jackybzhou",
                    "jordonxia",
                    "jubaoliang",
                    "kennyang",
                    "kevinjzhang",
                    "lewissi",
                    "lilylfhuang",
                    "lkunpengliu",
                    "loganqian",
                    "masonsqiao",
                    "morganzhang",
                    "neilsun",
                    "onismzhang",
                    "readingzhu",
                    "rickyrhuang",
                    "romyxu",
                    "ruosongli",
                    "russelltli",
                    "shaynewang",
                    "sheraleshen",
                    "shimershi",
                    "soniajyli",
                    "svenmanli",
                    "tinahhu",
                    "tinyjfyang",
                    "vincehuang",
                    "vivizwzhang",
                    "wizardcheng",
                    "yangxyang",
                    "yaozzzhao",
                    "yoneqiu",
                    "yuemingliu",
                    "zhiqshao"
                ],
                "DictI18nInfo": [
                    {
                        "Abstract": "安全稳定，高弹性的计算服务",
                        "Description": "稳定、安全、弹性、高性能的云端计算服务，实时满足您的多样性业务需求",
                        "Lang": "zh",
                        "Name": "云服务器",
                        "Site": 1,
                        "Type": 1
                    },
                    {
                        "Abstract": "",
                        "Description": "",
                        "Lang": "en",
                        "Name": "Cloud Virtual Machine",
                        "Site": 1,
                        "Type": 1
                    },
                    {
                        "Abstract": "",
                        "Description": "",
                        "Lang": "en",
                        "Name": "Cloud Virtual Machine",
                        "Site": 2,
                        "Type": 1
                    },
                    {
                        "Abstract": "",
                        "Description": "",
                        "Lang": "ko",
                        "Name": "Cloud Virtual Machine",
                        "Site": 2,
                        "Type": 1
                    },
                    {
                        "Abstract": "",
                        "Description": "",
                        "Lang": "jp",
                        "Name": "Cloud Virtual Machine",
                        "Site": 2,
                        "Type": 1
                    },
                    {
                        "Abstract": "",
                        "Description": "",
                        "Lang": "zh",
                        "Name": "云服务器",
                        "Site": 2,
                        "Type": 1
                    }
                ],
                "DictId": 2000,
                "EnName": "Cloud Virtual Machine",
                "FtId": 100,
                "FtName": "CSIG云与智慧产业事业群/云产品一部/计算产品中心",
                "Grade": "L3",
                "IntroPageLink": "https://cloud.tencent.com/product/cvm",
                "IntroPageStatus": 1,
                "IntroUpdateTime": "2024-07-03T18:11:06+08:00",
                "LifeCycleStatus": 4,
                "Name": "云服务器",
                "ParentId": 500,
                "ProductOwner": [
                    "candyxiao",
                    "chuangyuliu",
                    "elaineslli",
                    "gracecui",
                    "jasminewen",
                    "jennazhuang",
                    "lenxyliu",
                    "petzhou",
                    "qitinghuang"
                ],
                "Slug": "cvm",
                "SpaCode": "CD004051",
                "Type": 1,
                "Weight": 2030050000
            }
        ],
        "RequestId": "ad15d02c-e23a-4dd1-839d-e38c28bd4ec2",
        "Total": 1
    }
}
```

