**Example 1: 查询UIN 1122344554 灰度状态**



Input: 

```
tccli billing DescribeIsMeasureGrayUin --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "ba02cd16-9725-4ed3-932c-659b9fc05cb2",
        "Data": {
            "Uin": "1122344554",
            "QueryTime": "2022-03-29 00:00:00",
            "GrayVideoType": true,
            "GrayNewRecord": true
        }
    }
}
```

**Example 2: 查询 UIN 1223 当前的灰度状态**



Input: 

```
tccli billing DescribeIsMeasureGrayUin --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "ff49ab33-cf6f-4ff8-8cb7-d5902c9eebb4",
        "Data": {
            "Uin": "1223",
            "QueryTime": "2022-03-29 20:01:30",
            "GrayVideoType": true,
            "GrayNewRecord": true
        }
    }
}
```

