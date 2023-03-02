**Example 1: 火车票识别示例代码**

火车票识别

Input: 

```
tccli ocr TrainTicketOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "TicketNum": "17C060124",
        "StartStation": "南京南",
        "DestinationStation": "上海虹桥",
        "Date": "2017年12月23日10:33",
        "TrainNum": "G5",
        "Seat": "15车18A号",
        "Name": "周周",
        "Price": "134.50",
        "SeatCategory": "二等座",
        "ID": "3210231993****6499",
        "InvoiceType": "交通",
        "SerialNumber": "16804000071224C060124",
        "AdditionalCost": "2.00",
        "HandlingFee": "5.00",
        "LegalAmount": "贰元",
        "TicketStation": "成都客运段",
        "OriginalPrice": "83.50",
        "InvoiceStyle": "火车票补票",
        "ReceiptNumber": "",
        "IsReceipt": "0",
        "RequestId": "9084dec6-dae4-455f-976c-8e3609e86920"
    }
}
```

