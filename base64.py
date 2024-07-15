import base64
steps = ["plan", "code", "test", "delivery", "deploy", "monitor"]
encoded_steps = [base64.b64encode(step.encode()).decode() for step in steps]
for encoded_step in encoded_steps:
    print(f"b'{encoded_step}'")
