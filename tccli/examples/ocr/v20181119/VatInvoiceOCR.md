**Example 1: 增值税发票识别示例代码**



Input: 

```
tccli ocr VatInvoiceOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "VatInvoiceInfos": [
            {
                "Name": "价税合计(大写)",
                "Value": "捌拾玖圆玖角整"
            },
            {
                "Name": "发票代码",
                "Value": "012001100311"
            },
            {
                "Name": "发票号码",
                "Value": "No63591128"
            },
            {
                "Name": "发票名称",
                "Value": "天津增值税电子普通发票"
            },
            {
                "Name": "发票消费类型",
                "Value": "服务"
            },
            {
                "Name": "合计税额",
                "Value": "¥2.62"
            },
            {
                "Name": "合计金额",
                "Value": "¥87.28"
            },
            {
                "Name": "复核",
                "Value": "静静"
            },
            {
                "Name": "密码区1",
                "Value": "033-<<>7>616<-4+*-+4/5230604"
            },
            {
                "Name": "密码区2",
                "Value": "*/78+740454724/0<34*9/>61856"
            },
            {
                "Name": "密码区3",
                "Value": "29/-0651-2*91440-47386<535<5"
            },
            {
                "Name": "密码区4",
                "Value": "92<<9-9+-601452319091>67>--7"
            },
            {
                "Name": "小写金额",
                "Value": "¥89.90"
            },
            {
                "Name": "开票人",
                "Value": "丽丽"
            },
            {
                "Name": "开票日期",
                "Value": "2019年06月16日"
            },
            {
                "Name": "收款人",
                "Value": "张强"
            },
            {
                "Name": "是否有公司印章",
                "Value": "0"
            },
            {
                "Name": "机器编号",
                "Value": "499099606262"
            },
            {
                "Name": "校验码",
                "Value": "04656054380312409795"
            },
            {
                "Name": "省",
                "Value": "天津市"
            },
            {
                "Name": "购买方名称",
                "Value": "腾讯优图有限公司"
            },
            {
                "Name": "购买方识别号",
                "Value": "91440300MA55UJ6L44"
            },
            {
                "Name": "销售方名称",
                "Value": "深圳腾讯游戏有限公司"
            },
            {
                "Name": "销售方地址、电话",
                "Value": "天津经济技术开发区南港工业区综合服务区办公楼"
            },
            {
                "Name": "销售方开户行及账号",
                "Value": "招商银行股份有限公司天津自由贸易试验区分行122905939910401"
            },
            {
                "Name": "销售方识别号",
                "Value": "911201103409033300"
            },
            {
                "Name": "规格型号",
                "Value": "无"
            },
            {
                "Name": "单位",
                "Value": "次"
            },
            {
                "Name": "数量",
                "Value": "1"
            },
            {
                "Name": "单价",
                "Value": "87.28"
            },
            {
                "Name": "金额",
                "Value": "87.28"
            },
            {
                "Name": "税率",
                "Value": "3%"
            },
            {
                "Name": "税额",
                "Value": "2.62"
            },
            {
                "Name": "货物或应税劳务、服务名称",
                "Value": "客运服务费"
            },
            {
                "Name": "购买方地址、电话",
                "Value": ""
            },
            {
                "Name": "购买方开户行及账号",
                "Value": ""
            },
            {
                "Name": "备注",
                "Value": ""
            },
            {
                "Name": "联次",
                "Value": ""
            },
            {
                "Name": "是否代开",
                "Value": ""
            },
            {
                "Name": "成品油标志",
                "Value": ""
            },
            {
                "Name": "市",
                "Value": ""
            },
            {
                "Name": "服务类型",
                "Value": ""
            },
            {
                "Name": "通行费标志",
                "Value": ""
            },
            {
                "Name": "车船税",
                "Value": ""
            }
        ],
        "Items": [
            {
                "LineNo": "1",
                "Name": "",
                "Spec": "无",
                "Unit": "次",
                "Quantity": "1",
                "UnitPrice": "87.28",
                "AmountWithoutTax": "87.28",
                "TaxRate": "3%",
                "TaxAmount": "2.62"
            },
            {
                "LineNo": "2",
                "Name": "客运服务费",
                "Spec": "",
                "Unit": "",
                "Quantity": "",
                "UnitPrice": "",
                "AmountWithoutTax": "",
                "TaxRate": "",
                "TaxAmount": ""
            }
        ],
        "RequestId": "195835ab-c218-44af-bdd8-7d6c3104f924"
    }
}
```

