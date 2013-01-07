class IEHeaderMiddleware():
    def process_response(self, request, response):
        if "MSIE" in request.META.get("HTTP_USER_AGENT"):
            response["P3P"] = 'CP="IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT"'
            # print "got IE browser"
        else:
            pass
            # print "not IE browser"
        return response