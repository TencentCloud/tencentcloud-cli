**Example 1: 重加密接口示例**

对密文进行重新加密。

Input: 

```
tccli kms ReEncrypt --cli-unfold-argument  \
    --DestinationKeyId 23e80852-1e38-11e9-b129-5cb9019b4b01 \
    --CiphertextBlob Ade234dasdeEWdGVzdCUyMHBsYWlJJlIHL
```

Output: 
```
{
    "Response": {
        "CiphertextBlob": "g2F8eQk44QrTbfj09TL17AZyFPgs8BTtZe2j27Wuw1YzTBCxnd0T/gwFQSasmtzxZi6mmvD7DCjCE+LxJmdhXQ==-k-zJshb0kBH7C2J5I3XXbbEg==-k-o1O+7H9HFAzWbCkftO2ZtPKewS3diSB4zGKOJhMn7LcKRhYr",
        "KeyId": "23e80852-1e38-11e9-b129-5cb9019b4b01",
        "SourceKeyId": "23e80852-1e38-11e9-b129-5cb9019b0000",
        "ReEncrypted": true,
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```

