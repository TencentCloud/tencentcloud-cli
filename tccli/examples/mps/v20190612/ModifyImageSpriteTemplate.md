**Example 1: Modifying an image sprite generating template**



Input: 

```
tccli mps ModifyImageSpriteTemplate --cli-unfold-argument  \
    --Definition 10001 \
    --Name 'Image sprite generating template 1' \
    --Width 54 \
    --Height 96 \
    --SampleType Percent \
    --SampleInterval 10 \
    --RowCount 5 \
    --ColumnCount 10
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

