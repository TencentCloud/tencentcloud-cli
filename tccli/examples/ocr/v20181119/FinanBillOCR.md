**Example 1: 金融票据整单识别示例代码**

金融票据整单识别示例代码

Input: 

```
tccli ocr FinanBillOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg 
```

Output: 
```
{
    "Response": {
        "FinanBillInfos": [
            {
                "Name": "日期",
                "Value": "2018年10月11日"
            },
            {
                "Name": "出票全称",
                "Value": "李明"
            },
            {
                "Name": "出票账号",
                "Value": "6222024301069051406"
            },
            {
                "Name": "出票开户行",
                "Value": "工商银行四平支行"
            },
            {
                "Name": "收款人全称",
                "Value": "晓艾"
            },
            {
                "Name": "收款人账号",
                "Value": "4041968823461748"
            },
            {
                "Name": "收款开户行",
                "Value": "农业银行云南路支行"
            },
            {
                "Name": "大写金额",
                "Value": "贰仟圓整"
            },
            {
                "Name": "小写金额",
                "Value": "￥200000"
            },
            {
                "Name": "票据种类",
                "Value": "汇票"
            },
            {
                "Name": "票据张数",
                "Value": "1"
            },
            {
                "Name": "票据号码",
                "Value": "48000102"
            }
        ],
        "RequestId": "67ddf640-322a-48e9-8f23-1a868908fc54"
    }
}
```

