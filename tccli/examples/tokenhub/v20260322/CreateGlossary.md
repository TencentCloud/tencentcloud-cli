**Example 1: CreateGlossary**



Input: 

```
tccli tokenhub CreateGlossary --cli-unfold-argument  \
    --Name my-glossary \
    --Source zh \
    --Target en \
    --Description test glossary
```

Output: 
```
{
    "Response": {
        "CreatedAt": 1779967663,
        "GlossaryId": "14cf0f58e4f165ee414cbf43217650f2",
        "Name": "my-glossary",
        "RequestId": "46a9c46b-698b-42e8-9cc6-8a5604eeed01"
    }
}
```

