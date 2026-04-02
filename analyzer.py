def calculate_psr(first, first_resp, repeat_resp):
    if first == 0:
        return 0
    return (first_resp + repeat_resp) / first * 100


def analyze_kpi(row):
    results = {}

    # Call PSR
    call_psr = calculate_psr(
        row['Number of First Pagings in Calls (times)'],
        row['Number of Responses to First Pagings in Calls (times)'],
        row['Number of Responses to Repeated Pagings in Calls (times)']
    )

    # SMS PSR
    sms_psr = calculate_psr(
        row['Number of First Pagings in Short Message Service (times)'],
        row['Number of Responses to First Pagings in Short Message Service (times)'],
        row['Number of Responses to Repeated Pagings in Short Message Service (times)']
    )

    # PSI PSR
    psi_psr = calculate_psr(
        row['Number of First Pagings in PSI Service (times)'],
        row['Number of Responses to First Pagings in PSI Service (times)'],
        row['Number of Responses to Repeated Pagings in PSI Service (times)']
    )

    # 🔥 AI Logic (Rule-based)
    if call_psr < 80:
        results['CALL'] = "Low Call PSR → Check coverage / PCH / SDCCH"

    if sms_psr < 85:
        results['SMS'] = "Low SMS PSR → Check paging capacity or congestion"

    if psi_psr < 20:
        results['PSI'] = "Very Low PSI → Check SGSN / PS attach / core issue"

    return call_psr, sms_psr, psi_psr, results
