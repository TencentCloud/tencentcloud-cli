**Example 1: 小程序在线加固结果查询示例**

小程序在线加固结果查询示例

Input: 

```
tccli ms DescribeEncryptInstances --cli-unfold-argument  \
    --PlatformType 4 \
    --OrderType 1 \
    --EncryptOpType 1 \
    --EncryptState 1
```

Output: 
```
{
    "Response": {
        "EncryptResults": [
            {
                "AndroidResult": null,
                "IOSResult": null,
                "SDKResult": null,
                "AppletResult": {
                    "AppletInfo": {
                        "AppletJsUrl": "http://xxxxxxxxxxx.zip",
                        "AppletLevel": 1,
                        "Name": "test.zip"
                    },
                    "CostTime": 13,
                    "CreatTime": "2023-06-05 18:02:50",
                    "EncryptErrCode": 0,
                    "EncryptErrDesc": "",
                    "EncryptErrRef": "",
                    "EncryptPkgUrl": "https://xxxxxxxxxxxx/xxxxx/test.zip",
                    "EncryptState": 1,
                    "EncryptStateDesc": "加固成功",
                    "EndTime": "2023-06-05 18:03:21",
                    "OpUin": 700000154106,
                    "OrderId": "20230605_96ca291a-6e84-47eb-xxxxx-xxxxxx",
                    "ResourceId": "20230605_96ca291a-6e84-47eb-xxxxx-xxxxxx_0",
                    "ResultId": "6ef4eac9-badc-40d9-9796-569741849f95",
                    "StartTime": "2023-06-05 18:02:55"
                },
                "EncryptOpType": 1,
                "EncryptOpTypeDesc": "在线加固",
                "OrderType": 1,
                "OrderTypeDesc": "免费试用",
                "PlatformDesc": "applet小程序加固",
                "PlatformType": 4,
                "ResourceId": "xxxxxxx",
                "OrderId": "xxxxxxxxxxxxxx"
            }
        ],
        "RequestId": "3a25bb5e-6334-449c-b4bf-bbea1e673e3a",
        "TotalCount": 1
    }
}
```

**Example 2: 根据ResultId进行单记录查询**

根据ResultId进行单记录查询

Input: 

```
tccli ms DescribeEncryptInstances --cli-unfold-argument  \
    --ResultId 6ef4eac9-badc-40d9-9796-569741849f95
```

Output: 
```
{
    "Response": {
        "EncryptResults": [
            {
                "AndroidResult": null,
                "AppletResult": {
                    "AppletInfo": {
                        "AppletJsUrl": "http://xxxxxxx.zip",
                        "AppletLevel": 1,
                        "Name": "test.zip"
                    },
                    "CostTime": 13,
                    "CreatTime": "2023-06-05 18:02:50",
                    "EncryptErrCode": 0,
                    "EncryptErrDesc": "",
                    "EncryptErrRef": "",
                    "EncryptPkgUrl": "https://xxxxxxxx/test.zip",
                    "EncryptState": 1,
                    "EncryptStateDesc": "加固成功",
                    "EndTime": "2023-06-05 18:03:21",
                    "OpUin": 700000154106,
                    "OrderId": "20230605_96ca291a-6e84-47eb-xxxxxxx",
                    "ResourceId": "20230605_96ca291a-6e84-47eb-xxxxxxx_0",
                    "ResultId": "6ef4eac9-badc-40d9-9796-569741849f95",
                    "StartTime": "2023-06-05 18:02:55"
                },
                "EncryptOpType": 1,
                "EncryptOpTypeDesc": "在线加固",
                "IOSResult": null,
                "OrderType": 1,
                "OrderTypeDesc": "免费试用",
                "PlatformDesc": "applet小程序加固",
                "PlatformType": 4,
                "SDKResult": null,
                "ResourceId": "xxxxxxx",
                "OrderId": "xxxxxxxxxxxxxx"
            }
        ],
        "RequestId": "8019602c-b5be-4c90-932c-6e6f0e83c0bf",
        "TotalCount": 1
    }
}
```

**Example 3: 查询Android在线加固成功任务**

查询Android在线加固成功任务

Input: 

```
tccli ms DescribeEncryptInstances --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1 \
    --OrderField CreateTime \
    --OrderDirection asc \
    --PlatformType 1 \
    --OrderType 1 \
    --EncryptOpType 1 \
    --EncryptState 1
```

Output: 
```
{
    "Response": {
        "EncryptResults": [
            {
                "AndroidResult": {
                    "AndroidPlan": {
                        "AppPkgName": "com.One.WoodenLetter",
                        "AppType": "apk",
                        "EncryptParam": "{\"dex\":{\"enable\":1,\"antiprotect\":1,\"antirepack\":1,\"dexsig\":1,\"antimonitor\":1,\"ptrace\":1}}",
                        "PlanId": 11975
                    },
                    "AppMd5": "881ac0a49b3ae9967022217730cc0da8",
                    "AppName": "XXXX",
                    "AppPkgName": "com.One.TEST",
                    "AppSize": 4743475,
                    "AppType": "apk",
                    "AppUrl": "https://xxxxx/test.apk",
                    "AppVersion": "7.8.1",
                    "BindAppPkgName": "com.One.TEST",
                    "CostTime": 24,
                    "CreatTime": "2023-05-31 10:27:29",
                    "EncryptAppMd5": "710f9c41259d183bd1461817b6940b9e",
                    "EncryptAppSize": 5725152,
                    "EncryptErrCode": 0,
                    "EncryptErrDesc": "",
                    "EncryptErrRef": "",
                    "EncryptPkgUrl": "https://xxxxxxx/encrypt_dist/legu_20230531115709_xxxx.apk",
                    "EncryptState": 1,
                    "EncryptStateDesc": "加固成功",
                    "EndTime": "2023-05-31 11:57:15",
                    "OnlineToolVersion": "4.5.1.8",
                    "OpUin": 700000154106,
                    "OrderId": "20230530_0068940c-56d8-4bb8-9952-xxxx",
                    "OutputToolSize": 0,
                    "OutputToolUrl": "",
                    "OutputToolVersion": "",
                    "ResourceId": "20230530_0068940c-56d8-4bb8-9952-xxxx_0",
                    "ResultId": "1be49343-9bc4-40c7-9df1-1398e4743731",
                    "StartTime": "2023-05-31 10:27:29",
                    "ToolExpireTime": "0000-00-00 00:00:00",
                    "ToolOutputTime": "0000-00-00 00:00:00"
                },
                "AppletResult": null,
                "EncryptOpType": 1,
                "EncryptOpTypeDesc": "在线加固",
                "IOSResult": null,
                "OrderType": 1,
                "OrderTypeDesc": "免费试用",
                "PlatformDesc": "android加固",
                "PlatformType": 1,
                "SDKResult": null,
                "ResourceId": "xxxxxxx",
                "OrderId": "xxxxxxxxxxxxxx"
            }
        ],
        "RequestId": "f83ad565-fe48-4d45-bdb8-e84c72e67df5",
        "TotalCount": 7
    }
}
```

**Example 4: 查询Android输出工具任务结果**

查询Android输出工具任务结果

Input: 

```
tccli ms DescribeEncryptInstances --cli-unfold-argument  \
    --EncryptOpType 2 \
    --ResultId 0f869fd0-0fd0-44bd-95fc-06a15b50aa61
```

Output: 
```
{
    "Response": {
        "EncryptResults": [
            {
                "AndroidResult": {
                    "AndroidPlan": {
                        "AppPkgName": "com.One.TEST",
                        "AppType": "apk",
                        "EncryptParam": "{\n    \"dex\": {\n        \"enable\": 1,\n        \"antiprotect\": 1,\n        \"antirepack\": 1,\n        \"dexsig\": 1,\n        \"antimonitor\": 1,\n        \"ptrace\": 1\n    },\n    \"so\": {\n        \"enable\": 0,\n        \"ver\": \"1.3.3\",\n        \"file\": [\n            \"\"\n        ]\n    },\n    \"vmp\": {\n        \"enable\": 0,\n        \"ndkpath\": \"/xxx/android-ndk-r10e\",\n        \"profile\": \"XXX\",\n        \"mapping\": \"XXX\"\n    },\n    \"respro\": {\n        \"assets\": {\n            \"enable\": 0,\n            \"file\": [\n                \"assets/1.js\",\n                \"assets/2.jpg\"\n            ]\n        },\n        \"res\": {\n            \"enable\": 0,\n            \"file\": [\n                \"res/layout/1.xml\",\n                \"res/layout/2.xml\"\n            ]\n        }\n    }\n}",
                        "PlanId": 12011
                    },
                    "AppMd5": "",
                    "AppName": "",
                    "AppPkgName": "com.One.TEST",
                    "AppSize": 0,
                    "AppType": "apk",
                    "AppUrl": "",
                    "AppVersion": "",
                    "BindAppPkgName": "com.One.TEST",
                    "CostTime": 13,
                    "CreatTime": "2023-06-05 17:51:25",
                    "EncryptAppMd5": "",
                    "EncryptAppSize": 0,
                    "EncryptErrCode": 0,
                    "EncryptErrDesc": "",
                    "EncryptErrRef": "",
                    "EncryptPkgUrl": "",
                    "EncryptState": 1,
                    "EncryptStateDesc": "加固成功",
                    "EndTime": "2023-06-05 17:51:51",
                    "OnlineToolVersion": "",
                    "OpUin": 700000154106,
                    "OrderId": "20230605_52f727b2-8c5c-4069-b940-xxxxxxx",
                    "OutputToolSize": 109411473,
                    "OutputToolUrl": "https://xxxxxxxxx/xxxx-com.One.TEST-20230605.zip",
                    "OutputToolVersion": "4.5.1.8",
                    "ResourceId": "20230605_52f727b2-8c5c-4069-b940-xxxxxxx_0",
                    "ResultId": "0f869fd0-0fd0-44bd-95fc-06a15b50aa61",
                    "StartTime": "2023-06-05 17:51:33",
                    "ToolExpireTime": "2024-06-07 00:00:00",
                    "ToolOutputTime": "2023-06-05 17:51:47"
                },
                "AppletResult": null,
                "EncryptOpType": 2,
                "EncryptOpTypeDesc": "输出工具",
                "IOSResult": null,
                "OrderType": 2,
                "OrderTypeDesc": "按年收费",
                "PlatformDesc": "android加固",
                "PlatformType": 1,
                "SDKResult": null,
                "ResourceId": "xxxxxxx",
                "OrderId": "xxxxxxxxxxxxxx"
            }
        ],
        "RequestId": "59af19a2-9729-4397-a229-6ee8e8a15a1e",
        "TotalCount": 1
    }
}
```

