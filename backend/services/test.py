# # Use the native inference API to send a text message to Anthropic Claude.

# import boto3
# import json

# from botocore.exceptions import ClientError
# import os                      
# os.environ['AWS_BEARER_TOKEN_BEDROCK'] = "${bedrock-api-key-YmVkcm9jay5hbWF6b25hd3MuY29tLz9BY3Rpb249Q2FsbFdpdGhCZWFyZXJUb2tlbiZYLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFTSUEzTTQ2VVhJMlJRWklTVERYJTJGMjAyNTEyMTElMkZldS1ub3J0aC0xJTJGYmVkcm9jayUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMjExVDIzMzM1MVomWC1BbXotRXhwaXJlcz00MzIwMCZYLUFtei1TZWN1cml0eS1Ub2tlbj1JUW9KYjNKcFoybHVYMlZqRUM4YUNtVjFMVzV2Y25Sb0xURWlSekJGQWlFQTNNUFNwTU13ZTVBbGNEdDZMTUtIY2prQngwN05rVTVzc2xQeGFFeDJHJTJCY0NJQjhyMHhvVXZjY3dndWlLM0huJTJGeVFOTTh1emtzOEhIWkE3WDhGQmFkc1NRS3E0RENQbiUyRiUyRiUyRiUyRiUyRiUyRiUyRiUyRiUyRiUyRndFUUFCb01Oemd6TmpJM016WTVNREV6SWd6ckFWS0RaJTJGOWNLMHQ3USUyRjhxZ2dObkRBY3dyZklsQ2RDeElWZyUyRkMzTXZmMyUyQlVWUUlTeUd4JTJGYm12b3hCRExvWkdlWjRCTTRxVllVd0NRelIlMkJmdzNscnNsek8zd2tsTm1LUCUyQjVTSlo2JTJCaUppN1VDWkJ2bEp1WnpMRXglMkZxZnJHNG1yaW1RbmV6dGNsYmJ1TTBsbHB6JTJCVXlyV0xXQWQlMkI4TkJiclQ0b0lkcGliTnBxZG5aaldwV3FFJTJGbyUyRllpbGklMkY3JTJCTG1Cbk5tVDhPUXJKTzE0TyUyRnpnTm12THdPczl0ZWxGS2hUNTdpd3hZZzQ5WFh6ejlCYmpScklsSkJpdWZKWndlSTVKQVloOWJrb1olMkY0dHZIM09yRjlWUVJDakRqZ3dSaHFpTmFCSWVONDdablpaNCUyRjFWRm1qNEtIOGVDRjU5amt0YjVyd2ZGOGcydVFqSUR1JTJCJTJCR0pDeW9HRm5tMkttamVOcjZjVWlmdk02WTFqZCUyQnNvckI4bTM0T1duU2lZJTJCbzNsZUNQSEFkRE1HdHVrWUFveVBEdXhZMXg5OEFZZWZYZkpxV0VXcU5mb1JTc2RJR2FsSXFPbmNuckdCd0hkdm5yZUtUTDZCZlhyc0NOVHNwOUhSUzA1VVcwb241WW41ZkZVUEdiQ04lMkJPJTJCOTJQZUFWODUlMkZhbHBONXpjZHd3NjF5RyUyRmFJaDMlMkJzY1I0UjlCQmhVR3BEYVkwakNMOU96SkJqcmVBb1hDVDdOTTU2NkowU0pMeG42R2htbDAlMkJPRnRPZEdnZ1FsSFdnRXNEOFpRNCUyRkk4djExRWN4WWlLRWFCQ09wbGlRUmtCcEpuZERqRkVOODhGaDR0OGx0Um1BMHV0dFd3cVg3WXhTVWU0ZCUyQllCJTJCcTJBVGh2V3phaDQ3aVhwM1BIa1QwcjJQWnZaaFR1SFlIR2RNam55cHZYbmtRQVMwZnMxWiUyQjRkUlN0UzBRUno0V1ZORk9ObjZydTMycjduRDR0ZmJ6OXlNMlJQZmg0UHl5Wnh0eTBjRnNJMGdVTlU0TUFjYTlOaXNNOTd6RnZyR0lGZzdCWHpLN2tDJTJGRmdQeiUyRnlubyUyRlBGYTd4Mno0YjR0cDhReTZCMnYzUmtwMXRCYnIwVnNQQVc4NllqWm43NkNGV1JLUCUyQjlRemo1VFV6elM1N1BXTmtsJTJGMHAlMkJvZzhtZEMzaEdNemc0RnZnS2klMkZxdXclMkJqczVBdjRGM1FVb0Zaem1kQlhqaHZ5SkhCRHZZN29ybDZCMzA4YjVCdmlHY2pUVSUyRlBMb3BhM1RvT2clMkJBdWglMkJBS1olMkJxQ1JFMkIxemtNNHBIckdxemVKQWJJWGltMXdkcFpSWmxFeW5GTGx6T1FqMWdxakJPJlgtQW16LVNpZ25hdHVyZT03OGE5MDQwZjYwZmZmZGZlZjkzZTE2YTIwMjRiNjdiN2YwODJhM2JhNTQ3ZjBkMjc1Y2YxNTIwMWEzYzI1ODhiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZWZXJzaW9uPTE=}"

# # Create a Bedrock Runtime client in the AWS Region of your choice.
# client = boto3.client("bedrock-runtime", region_name="us-east-1")

# # Set the model ID, e.g., Claude 3 Haiku.
# model_id = "anthropic.claude-3-haiku-20240307-v1:0"

# # Define the prompt for the model.
# prompt = "Describe the purpose of a 'hello world' program in one line."

# # Format the request payload using the model's native structure.
# native_request = {
#     "anthropic_version": "bedrock-2023-05-31",
#     "max_tokens": 512,
#     "temperature": 0.5,
#     "messages": [
#         {
#             "role": "user",
#             "content": [{"type": "text", "text": prompt}],
#         }
#     ],
# }

# # Convert the native request to JSON.
# request = json.dumps(native_request)

# try:
#     # Invoke the model with the request.
#     response = client.invoke_model(modelId=model_id, body=request)

# except (ClientError, Exception) as e:
#     print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
#     exit(1)

# # Decode the response body.
# model_response = json.loads(response["body"].read())

# # Extract and print the response text.
# response_text = model_response["content"][0]["text"]
# print(response_text)




