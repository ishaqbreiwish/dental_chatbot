from langchain_query import query_with_langchain

query = "how to maintain gum health"
response = query_with_langchain(query)
print(response)