# DataFrame QuickView

**DataFrame QuickView** is a Python package that extends pandas DataFrame functionality to easily display and visualize DataFrames in a web-based environment. This package is an experiment in paired programming with GPT-4. It is built using Flask and allows users to view paginated DataFrames and interactively generate histograms based on the selected columns.

![Diagram](diagram.png)

## Features

### Phase 1

- Extend pandas DataFrame with `quickview()` method
- Display paginated DataFrame in a web browser
- Create an interactive dropdown and button combination populated with DataFrame columns
- Generate histograms based on the selected column when the button is pressed

### Phase 1 Technical Overview

- Flask server: Represents the backend server running the Flask application, which serves the paginated DataFrame and processes the histogram data.
- DataFrame display: The component in the web browser that shows the paginated DataFrame.
- Column selection: The dropdown and button combination that allows users to select a column for generating the histogram.
- Histogram generation: The component responsible for creating a histogram based on the selected column.

Interactions:

- Flask server sends the paginated DataFrame to the DataFrame display.
- User selects a column in the Column selection component.
- User clicks the button in the Column selection component.
- Flask server receives the selected column and processes the histogram data.
- Histogram generation component receives the data and displays the histogram.

## Usage

1. Install the package using pip:

```
pip install dataframe-quickview
```


2. Import the package and use the `quickview()` method on a pandas DataFrame object:

```python
import pandas as pd
from dataframe_quickview import quickview

data = {'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10], 'C': [3, 6, 9, 12, 15]}
df = pd.DataFrame(data)

df.quickview()
```

This will start the Flask server and open the browser to view the paginated DataFrame and interactive histogram.

## Contributing

We welcome contributions to this project. However, please note that all code added to the project should be written primarily by Language Models (LLMs) to maintain the experimental nature of this project.

## License

This project is licensed under the MIT License.