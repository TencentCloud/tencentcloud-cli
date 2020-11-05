**Example 1: Querying Price for Cloud Disk  Expansion to 200G**



Input: 

```
tccli cbs InquiryPriceResizeDisk --cli-unfold-argument  \
    --DiskId disk-dw0bbzws\
    --DiskSize 200
```

Output: 
```
{
    "Response": {
        "DiskPrice": {
            "DiscountPrice": 210.09,
            "OriginalPrice": 210.09
        },
        "RequestId": "2ba7b520-ddb4-f5ea-34d1-5a1f80434911"
    }
}
```

