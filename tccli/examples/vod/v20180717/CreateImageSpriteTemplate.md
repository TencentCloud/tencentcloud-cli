**Example 1: Creating an image sprite generating template**



Input: 

```
tccli vod CreateImageSpriteTemplate --cli-unfold-argument  \
    --Name 'Image sprite generating template 1'\
    --Width 128\
    --Height 128\
    --SampleType Percent\
    --SampleInterval 10\
    --RowCount 5\
    --ColumnCount 10
```

Output: 
```
{
    "Response": {
        "Definition": 1008,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

