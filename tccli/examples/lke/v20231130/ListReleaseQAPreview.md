**Example 1: 发布问答预览**



Input: 

```
tccli lke ListReleaseQAPreview --cli-unfold-argument  \
    --BotBizId 1694921462777761792 \
    --PageNumber 1 \
    --PageSize 10 \
    --Query  \
    --ReleaseBizId 0 \
    --StartTime 0 \
    --EndTime 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Action": 3,
                "ActionDesc": "删除",
                "FileName": "",
                "FileType": "",
                "Message": "",
                "QaBizId": "161612",
                "Question": "aaaa",
                "ReleaseStatus": 0,
                "Source": 3,
                "SourceDesc": "手动录入",
                "UpdateTime": "1701264450"
            },
            {
                "Action": 3,
                "ActionDesc": "删除",
                "FileName": "",
                "FileType": "",
                "Message": "",
                "QaBizId": "161738",
                "Question": "问题1",
                "ReleaseStatus": 0,
                "Source": 2,
                "SourceDesc": "批量导入",
                "UpdateTime": "1701422596"
            },
            {
                "Action": 3,
                "ActionDesc": "删除",
                "FileName": "",
                "FileType": "",
                "Message": "",
                "QaBizId": "161739",
                "Question": "问题2",
                "ReleaseStatus": 0,
                "Source": 2,
                "SourceDesc": "批量导入",
                "UpdateTime": "1701427533"
            },
            {
                "Action": 3,
                "ActionDesc": "删除",
                "FileName": "",
                "FileType": "",
                "Message": "",
                "QaBizId": "161740",
                "Question": "qq",
                "ReleaseStatus": 0,
                "Source": 2,
                "SourceDesc": "批量导入",
                "UpdateTime": "1701670093"
            },
            {
                "Action": 1,
                "ActionDesc": "新增",
                "FileName": "深圳市最低生活保障办法.docx",
                "FileType": "docx",
                "Message": "",
                "QaBizId": "162463",
                "Question": "深圳市最低生活保障办法何时开始施行？",
                "ReleaseStatus": 0,
                "Source": 1,
                "SourceDesc": "深圳市最低生活保障办法.docx",
                "UpdateTime": "1700550874"
            },
            {
                "Action": 1,
                "ActionDesc": "新增",
                "FileName": "",
                "FileType": "",
                "Message": "",
                "QaBizId": "1731558661913706496",
                "Question": "a",
                "ReleaseStatus": 0,
                "Source": 3,
                "SourceDesc": "手动录入",
                "UpdateTime": "1701670760"
            }
        ],
        "RequestId": "0260ac98-913d-4aab-9276-8a045f627e4e",
        "Total": "6"
    }
}
```

