from googlesearch import search

def terminal_search(query, num_results=5):
    try:
        search_results = search(query, num_results=num_results, advanced=True)
        print("\nSearch Results:")
        for i, result in enumerate(search_results, start=1):
            print(f"{i}. {result}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Simple Terminal Internet Search Engine")
    print("---------------------------------------------")
    while True:
        search_query = input("Enter your search query (type 'exit' to quit): ")
        
        if search_query.lower() == 'exit':
            break

        num_results = int(input("Enter the number of results to display (default is 5): ") or 5)

        terminal_search(search_query, num_results)

    print("Exiting the search engine.")