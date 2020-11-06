**Example 1: 续费专业版**

续费专业版，用于包年包月计费模式进行续费

Input: 

```
tccli yunjing RenewProVersion --cli-unfold-argument  \
    --ChargePrepaid.Period 1 \
    --Quuid add4a78a-0d59-11e8-b7ab-00e081e1a5c5
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

