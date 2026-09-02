**Example 1: 以加密请求体方式创建请求**



Input: 

```
tccli essbasic CreateRequestWithEncryption --cli-unfold-argument  \
    --RequestAction ChannelDescribeFlowComponents \
    --ApplicationId yD****************************** \
    --IV mJc2aKe4B71d9p62y6bp2A== \
    --EncryptedData riUP2CKf+QGCfN9VMjTgCbsPidmXJulBUD8jxdg3YZwecWCF1CTg+4zB1nEICbGPRedPjF0+zZ1ybTDEc/xG/nQ5J7n4+uNiWCCOqRsjDcwzoD1gZ+y1W++qdjjCns/z8SMxciKmSS7h/cL5kwUARg== \
    --EncryptionSignature vzOw7yV+oAaYBmpbDDGfl7OGxuN3M38IjpJG/mTnEzE=
```

Output: 
```
{
    "Response": {
        "EncryptedData": "vPMmeHGhjZOh5uBcnTmcsgamkGHPrwVCcf9ifqAp03M/pdi3yalY86ytw5fL1VbUg+97j/DZpcejEld5mq5Qa1Sk+L6WIgKc8Wc2Bu5LNB5ktM6b5Xy09MXdWvxQV0l40XlhEEQ2bNqI/G7AfJpRLxNLRbK2VH/DFy+ga8o6snHQE3OojM3ZQgM6gLcQ/6MudNChL95Bf3SEWnrr4lqKLdZWJxOOj/XR/iQD/VSr1XE=",
        "EncryptionSignature": "ReXDVVwCHf1bgoW/al4NAs9r2dzWWfmV0zVNDl1Kne8=",
        "IV": "xJVzDCv28EtziawMOIhgGA==",
        "RequestId": "b91d7791-644f-4404-984b-b0c8a10e58b0"
    }
}
```

