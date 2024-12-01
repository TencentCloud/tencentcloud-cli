**Example 1: 查询导播台的水印列表**



Input: 

```
tccli live DescribeCasterMarkPicInfos --cli-unfold-argument  \
    --CasterId 1234
```

Output: 
```
{
    "Response": {
        "MarkPicInfos": [
            {
                "MarkPicIndex": 1,
                "MarkPicId": 0,
                "MarkPicUrl": "https://www.example.com/pic/example.jpg",
                "MarkPicWidth": 0.2,
                "MarkPicHeight": 0.2,
                "MarkPicLocationX": 0,
                "MarkPicLocationY": 0.3,
                "Description": "",
                "IsEqualProportion": false
            }
        ],
        "RequestId": "4b154257-a7ba-4371-91f2-40f44ee83f5c"
    }
}
```

