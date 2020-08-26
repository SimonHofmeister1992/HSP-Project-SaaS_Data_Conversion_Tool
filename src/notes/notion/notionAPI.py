#from notion.client import NotionClient
#from notion.block import TodoBlock
#from notion.collection import Collection
#
## Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on #Notion.so
#client = #NotionClient(token_v2="2ba3f0ef5acbfc6296cda29c01958e6ce8558cc6386ce6bc823b6ec952fa63082898567715b0013359a7f60dc7664b8f7acab4988105eb3d68c9e5951349ef6da8bd073d00735102cfbd79ba18de")
#
## Replace this URL with the URL of the page you want to edit
#page = client.get_block("https://www.notion.so/4d9514bea6a74f68963116dd7824aa38?#v=32c0ab4841714d09a01ee13be1565047")
#page2 = client.get_collection_view("https://www.notion.so/4d9514bea6a74f68963116dd7824aa38?#v=32c0ab4841714d09a01ee13be1565047")
#
##################################################################################
#print("###############################################################")
#print("Page data")
#print(page)
#
##################################################################################
#print("###############################################################")
#print("Query of Collection")
#result = page2.default_query().execute()
#for row in result:
#    print(row.id)
#    temp = client.get_block(row.id)
#    for block in temp.children:
#        print(block.title)
#
##################################################################################  
#print("###############################################################")
#print("Iterate in page tree")
#for child in page.children:
#    print(child.id)
#
##################################################################################
#print("###############################################################")
#print("Iterate over block in one page")
#page3 = client.get_block("https://www.notion.so/4d9514bea6a74f68963116dd7824aa38?#v=32c0ab4841714d09a01ee13be1565047&p=d04fb2980f05451fb42c35f623042d2d")
#for child in page3.children:
#    print(child.title)
#
##################################################################################     
#print("###############################################################")
#print("Iterate over two levels")      
#for child1 in page3.children:
#    test = child1.id
#    test2 = client.get_block(test)
#    for child in test2.children:
#        print(child.title)
#        
##################################################################################
#print("###############################################################")
#print("Query of Collection")
#result = page2.default_query().execute()
#for row in result:
#    print(row.id)
#    temp = client.get_block(row.id)
#    print("----------------------------------------------------------------------------------")
#    print(temp.title)
#    print(temp._get_record_data())
#    for block in temp.children:
#        print("  ", block.title)
#        print("  ", block._get_record_data())
#        
#
