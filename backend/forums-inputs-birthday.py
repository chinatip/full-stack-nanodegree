# Forums and Inputs
import webapp2
months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
month_abbvs = dict((m[:3].lower(), m) for m in months)
          
def valid_month(month):
    if month:
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)

def valid_day(day):
    if not day.isdigit():
        return None
    day = int(day)
    if day > 0 and day < 32:
        return day
    else:
        return None

def valid_year(year):
    if year.isdigit() and year:
        year = int(year)
        if year >= 1900 and year <= 2020:
            return year
        return None

def escape_html(s):
    for (i, o) in (("&", "&amp;"), 
                    (">", "&gt;"),
                    ("<", "&lt;"),
                    ('"', "&quot;")):
        s = s.replace(i, o)
    return s

form = """
<form method="post">
    What is your birthday?
    <br>
    Month
    <input type="text" name="month" value="%(month)s">
    Day
    <input type="text" name="day" value="%(day)s">
    Year
    <input type="text" name="year" value="%(year)s">
    <br>
    <div style="color: red"> %(error)s</div>
    <br>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error": error, "month" : escape_html(month), "day" : escape_html(day), "year" : escape_html(year)})

    def get(self):
        self.write_form()
    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not (month and day and year):
            self.write_form("That doesn't look valid to me, friend.", user_month, user_day, user_year)
        else:
            self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! That's a totally valid day!")

app = webapp2.WSGIApplication([
    ('/', MainPage), ('/thanks', ThanksHandler)
], debug=True)