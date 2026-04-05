**Example 1: 发布示例**



Input: 

```
tccli wedata ListExperiments --cli-unfold-argument  \
    --WorkspaceId 17623497097012366
```

Output: 
```
{
    "Response": {
        "Data": {
            "List": [
                {
                    "CreationTime": "1764765148817",
                    "CreatorName": "600000561778",
                    "CreatorUid": "600000561778",
                    "Description": "",
                    "ExperimentId": "6",
                    "Name": "test11111",
                    "Type": "MACHINE_LEARNING"
                },
                {
                    "CreationTime": "1762514171401",
                    "CreatorName": "wedata30-dev@tencent.com",
                    "CreatorUid": "700002164618",
                    "Description": "test for totalcount",
                    "ExperimentId": "4",
                    "Name": "garrizhang_test_v1",
                    "Type": "MACHINE_LEARNING"
                },
                {
                    "CreationTime": "1762413627215",
                    "CreatorName": "",
                    "CreatorUid": "",
                    "Description": "",
                    "ExperimentId": "3",
                    "Name": "iris-classification",
                    "Type": ""
                },
                {
                    "CreationTime": "1762345562986",
                    "CreatorName": "",
                    "CreatorUid": "",
                    "Description": "",
                    "ExperimentId": "2",
                    "Name": "1",
                    "Type": ""
                },
                {
                    "CreationTime": "1762335682543",
                    "CreatorName": "wedata30-dev@tencent.com",
                    "CreatorUid": "700002164618",
                    "Description": "213",
                    "ExperimentId": "1",
                    "Name": "sdf",
                    "Type": "MACHINE_LEARNING"
                },
                {
                    "CreationTime": "1762329920044",
                    "CreatorName": "",
                    "CreatorUid": "",
                    "Description": "",
                    "ExperimentId": "0",
                    "Name": "Default",
                    "Type": ""
                }
            ],
            "NextPageToken": ""
        },
        "RequestId": "5ba15f0e-12b0-4cb1-a92c-6843c33bc05e"
    }
}
```

