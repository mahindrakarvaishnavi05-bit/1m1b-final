import streamlit as st

st.title("♻️ AI Waste Segregation Guide")

st.markdown("### SDG 12: Responsible Consumption and Production")
st.write(
    "This tool helps users segregate waste correctly for better recycling and sustainability."
)

items = st.text_area(
    "Enter Waste Items (one item per line)",
    height=150
)

if st.button("Classify All Items"):

    wet = []
    dry = []
    hazardous = []
    ewaste = []
    unknown = []

    waste_list = items.split("\n")

    for waste in waste_list:

        waste = waste.strip().lower()

        if waste == "":
            continue

        # Wet Waste
        if (
            "banana" in waste
            or "apple" in waste
            or "fruit" in waste
            or "vegetable" in waste
            or "food" in waste
            or "peel" in waste
            or "tea leaves" in waste
            or "flower" in waste
            or "leftover" in waste
        ):
            wet.append(waste)

        # Dry Waste
        elif (
            "plastic" in waste
            or "paper" in waste
            or "newspaper" in waste
            or "cardboard" in waste
            or "pencil" in waste
            or "pen" in waste
            or "bottle" in waste
            or "notebook" in waste
            or "magazine" in waste
            or "glass" in waste
        ):
            dry.append(waste)

        # Hazardous Waste
        elif (
            "battery" in waste
            or "medicine" in waste
            or "chemical" in waste
            or "paint" in waste
            or "bulb" in waste
            or "tube light" in waste
        ):
            hazardous.append(waste)

        # E-Waste
        elif (
            "mobile" in waste
            or "phone" in waste
            or "charger" in waste
            or "laptop" in waste
            or "cable" in waste
            or "keyboard" in waste
            or "mouse" in waste
            or "earphones" in waste
        ):
            ewaste.append(waste)

        else:
            unknown.append(waste)

    # Summary
    st.subheader("📊 Waste Summary")

    st.write("🟢 Wet Waste Items:", len(wet))
    st.write("🔵 Dry Waste Items:", len(dry))
    st.write("🔴 Hazardous Waste Items:", len(hazardous))
    st.write("💻 E-Waste Items:", len(ewaste))
    st.write("❓ Unknown Waste Items:", len(unknown))

    # Wet Waste
    if wet:
        st.success("🟢 Wet Waste")
        for item in wet:
            st.write("-", item)

    # Dry Waste
    if dry:
        st.info("🔵 Dry Waste")
        for item in dry:
            st.write("-", item)

    # Hazardous Waste
    if hazardous:
        st.warning("🔴 Hazardous Waste")
        for item in hazardous:
            st.write("-", item)

        st.info(
            "Dispose hazardous waste at authorized collection centers."
        )

    # E-Waste
    if ewaste:
        st.success("💻 E-Waste")
        for item in ewaste:
            st.write("-", item)

        st.info(
            "Take e-waste to a certified e-waste recycling facility."
        )

    # Unknown Waste
    if unknown:
        st.error("❓ Unknown Waste")
        for item in unknown:
            st.write("-", item)

    # Impact Section
    st.markdown("---")
    st.subheader("🌍 Environmental Impact")

    st.success(
        "Proper waste segregation improves recycling efficiency, "
        "reduces landfill waste, minimizes pollution, and supports "
        "SDG 12: Responsible Consumption and Production."
    )