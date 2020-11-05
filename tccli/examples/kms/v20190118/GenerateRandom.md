**Example 1: Generating a random number**

This example shows you how to generate a random number.

Input: 

```
tccli kms GenerateRandom --cli-unfold-argument  \
    --NumberOfBytes 16
```

Output: 
```
{
    "Response": {
        "Plaintext": "17mvQgMl0sbM7OAJ7fpLsA==",
        "RequestId": "6010cd3d-a85a-4e00-b37b-22606d017420"
    }
}
```

