# Anomaly Detection: Extreme Usages & Fraud

Anomaly detection involves identifying unusual behaviors or events in a dataset, often linked to users or transactions, to detect potential fraud or extreme usage patterns.

---

## Key Concepts

### **Extreme Usages**

Refers to abnormal patterns in the use of services or products, such as:

-   Excessive transactions.
-   Overconsumption of resources.
-   Sudden changes in usage habits.

### **Fraud**

Encompasses malicious or deceptive activities, often aimed at financial gain or misuse of services.

---

## Objective

The primary goal of anomaly detection is to quickly identify extreme or fraudulent activities to prevent financial losses or service disruptions.

---

## Data Sources

The data is structured into two tables:

### **1. Fraud Table**

Contains data on suspicious or fraudulent calls and activities, enabling the detection of abnormal patterns compared to normal user behavior.

#### **Columns:**

-   **`Call_Type`**: Type of call (e.g., voice, SMS, data).
-   **`Charging_Tm`**: Billing duration of the call.
-   **`Call_Duration`**: Call length in seconds or minutes.
-   **`Telesrvc`**: Telecom service used (e.g., voice, data).
-   **`Location`**: Geographical location of the call.
-   **`A_Num`**: Caller’s phone number.
-   **`B_Num`**: Recipient’s phone number.
-   **`cell_id`**: Cellular tower ID used for the call.
-   **`IMEI`**: Unique identifier for the caller's mobile device.
-   **`TAC`**: Code identifying the mobile device model.
-   **`DESTINATION`**: Call destination (e.g., local, international).
-   **`DESTINATION_CAT`**: Destination category (e.g., type of call).
-   **`MU_HANDSET_DUAL_SIM`**: Indicates if the handset is dual-SIM.
-   **`MU_Device_type_Segment`**: Type of device (e.g., smartphone, feature phone).
-   **`MU_HANDSET_MOBILE_TECH`**: Mobile technology (e.g., 4G, 5G).

These columns help identify anomalies and unusual behaviors in calls and services.

---

### **2. Non-Fraud Table**

Contains data on non-suspicious calls, serving as a baseline for comparison with fraudulent data to define normal behavior.

#### **Columns:**

-   **`Call_Type`**: Type of call with additional classifications:
    -   **`0`**: Voice Out.
    -   **`7`**: SMS In.
    -   **`6`**: SMS Out.
    -   **`2`**: Voice-RF In.
    -   **`100`**: Voice-F Out (e.g., transferred call).
-   **`Charging_Tm`**: Billing duration of the call.
-   **`Call_Duration`**: Call length in seconds or minutes.
-   **`Telesrvc`**: Telecom service used (e.g., voice, data).
-   **`LOCATION`**: Geographical location of the call.
-   **`A_Num`**: Caller’s phone number.
-   **`B_Num`**: Recipient’s phone number.
-   **`cell_id`**: Cellular tower ID used for the call.
-   **`IMEI`**: Unique identifier for the caller's mobile device.
-   **`TAC`**: Code identifying the mobile device model.
-   **`DESTINATION`**: Call destination (e.g., local, international).
-   **`DESTINATION_CAT`**: Destination category (e.g., type of call).
-   **`MU_HANDSET_DUAL_SIM`**: Indicates if the handset is dual-SIM.
-   **`MU_Device_type_Segment`**: Type of device (e.g., smartphone, feature phone).
-   **`MU_HANDSET_MOBILE_TECH`**: Mobile technology (e.g., 4G, 5G).
