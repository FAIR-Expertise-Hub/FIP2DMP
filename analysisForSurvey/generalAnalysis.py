from main import questions, df

# Analyze the data for each question
for question in questions:
    print(f"Question: {question['name']}")
    print(f"Type: {question['type']}")
    print(f"Text: {question['text']}")
    values = df.loc[question['name']].values
    for volunteer, value in zip(df.columns, values):
        print(f"{volunteer}:")
        if isinstance(value, (list, tuple)):
            for item in value:
                print(f"  - {item}")
        else:
            print(f"  - {value}")
    print("\n")