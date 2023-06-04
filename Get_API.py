import webbrowser


# Define the URL of the webpage where the API is generated
api_generation_url = "https://salinaqi57.atlassian.net/jira/your-work"

# Open the URL in the default web browser
webbrowser.open(api_generation_url)

# Wait for user interaction or page load delay

# Once the API is generated, retrieve it from the webpage
#api_element_id = "deep-dive-card-content--project-name-heading"  # ID of the HTML element containing the API value

# Assuming the webpage uses JavaScript to generate the API value,
# you can use a delay or user interaction to allow time for the API to be generated
# Alternatively, you can use a library like Selenium for more complex scenarios

# Retrieve the API value from the webpage
api_value = input("Please enter the generated API value: ")

# Print the API value
print("Generated API:", api_value)
