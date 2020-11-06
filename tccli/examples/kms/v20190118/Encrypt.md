**Example 1: 加密接口示例**

使用CMK对小于4KB的数据加密。

Input: 

```
tccli kms Encrypt --cli-unfold-argument  \
    --KeyId 23e80852-1e38-11e9-b129-5cb9019b4b01 \
    --Plaintext dGVzdCUyMHBsYWluJTIwdGV4dA
```

Output: 
```
{
    "Response": {
        "RequestId": "816c6886-2147-4ee7-86f0-9400a7a398a5",
        "KeyId": "9999aed0-4956-11e9-bc70-5254005e86b4",
        "CiphertextBlob": "g2F8eQk44QrTbfj09TL17AZyFPgs8BTtZe2j27Wuw1YzTBCxnd0T/gwFQSasmtzxZi6mmvD7DCjCE+LxJmdhXQ==-k-zJshb0kBH7C2J5I3XXbbEg==-k-o1O+7H9HFAzWbCkftO2ZtPKewS3diSB4zGKOJhMn7LcKRhYr"
    }
}
```

