**Example 1: 网约车行程单识别示例代码**



Input: 

```
tccli ocr RecognizeOnlineTaxiItineraryOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "OnlineTaxiItineraryInfos": [
            {
                "Name": "行程单分类",
                "Value": "滴滴出行-行程单"
            },
            {
                "Name": "行程开始日期",
                "Value": "2021年04月09日"
            },
            {
                "Name": "申请日期",
                "Value": "2021年04月16日"
            },
            {
                "Name": "行程结束日期",
                "Value": "2021年04月09日"
            },
            {
                "Name": "手机号",
                "Value": "18600208392"
            },
            {
                "Name": "合计金额",
                "Value": "154.08元"
            },
            {
                "Name": "车型",
                "Value": "滴滴礼橙专车"
            },
            {
                "Name": "上车时间",
                "Value": "04-0922:44周五"
            },
            {
                "Name": "城市",
                "Value": "北京市"
            },
            {
                "Name": "起点",
                "Value": "富华大厦C座-正门"
            },
            {
                "Name": "终点",
                "Value": "旧宫润枫锦尚-东门"
            },
            {
                "Name": "里程",
                "Value": "19.4"
            },
            {
                "Name": "金额",
                "Value": "154.08"
            }
        ],
        "RequestId": "533f9062-9ef3-47c6-b235-fcc1975c94c9"
    }
}
```

