**Example 1: 生成数据密钥示例**

使用指定的CMK生成Datakey。

Input: 

```
tccli kms GenerateDataKey --cli-unfold-argument  \
    --KeyId 23e80852-1e38-11e9-b129-5cb9019b4b01 \
    --KeySpec AES_256
```

Output: 
```
{
    "Response": {
        "RequestId": "fe11aa29-0cc2-4204-bfea-6ebb30cc00d7",
        "KeyId": "23e80852-1e38-11e9-b129-5cb9019b4b01",
        "Plaintext": "uW9wqntw+FAgnfsIrxOpOA==",
        "CiphertextBlob": "g2F8eQk44QrTbfj09TL17AZyFPgs8BTtZe2j27Wuw1YzTBCxnd0T/gwFQSasmtzxZi6mmvD7DCjCE+LxJmdhXQ==-k-fKVP3WIlGpg8m9LMW4jEkQ==-k-h/nUfRbaTUY7/KWXwuSK1Py+ZFRTK5WQiUz6yQE5XBFUN3UwPOUbl8P3A3caow2rlqTjUw=="
    }
}
```

