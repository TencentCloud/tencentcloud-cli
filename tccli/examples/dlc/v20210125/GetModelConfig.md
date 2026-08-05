**Example 1: 调用示例**



Input: 

```
tccli dlc GetModelConfig --cli-unfold-argument  \
    --ModelUid m-bge-reranker-v2-m3-6a223aba-2e20 \
    --ModelVersion v1
```

Output: 
```
{
    "Response": {
        "ConfigJson": "{\n  \"_name_or_path\": \"BAAI/bge-m3\",\n  \"architectures\": [\n    \"XLMRobertaForSequenceClassification\"\n  ],\n  \"attention_probs_dropout_prob\": 0.1,\n  \"bos_token_id\": 0,\n  \"classifier_dropout\": null,\n  \"eos_token_id\": 2,\n  \"hidden_act\": \"gelu\",\n  \"hidden_dropout_prob\": 0.1,\n  \"hidden_size\": 1024,\n  \"id2label\": {\n    \"0\": \"LABEL_0\"\n  },\n  \"initializer_range\": 0.02,\n  \"intermediate_size\": 4096,\n  \"label2id\": {\n    \"LABEL_0\": 0\n  },\n  \"layer_norm_eps\": 1e-05,\n  \"max_position_embeddings\": 8194,\n  \"model_type\": \"xlm-roberta\",\n  \"num_attention_heads\": 16,\n  \"num_hidden_layers\": 24,\n  \"output_past\": true,\n  \"pad_token_id\": 1,\n  \"position_embedding_type\": \"absolute\",\n  \"torch_dtype\": \"float32\",\n  \"transformers_version\": \"4.38.1\",\n  \"type_vocab_size\": 1,\n  \"use_cache\": true,\n  \"vocab_size\": 250002\n}",
        "ModelName": "bge-reranker-v2-m3",
        "RequestId": "55918bd9-400d-46d0-abc6-b927be3c9ca3"
    }
}
```

