#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re
import cgi

def build_page():

    form= """<html><head>
        <style>
            .error {
                color: red;
            }
        </style>
    </head>
    <body>
    <h1>Signup</h1>
        <form method="post">

                <tbody><tr>
                    <td><label for="username">Username</label></td>
                    <td>
                        <input name="username" type="text" value="%(username)s" />
                        <span class="error">%(user_error)s</span>
                        <br>
                    </td>
                </tr>
                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" type="password"/>
                        <span class="error">%(pw_error)s</span>
                        <br>
                    </td>
                </tr>
                <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify" type="password" />
                        <span class="error">%(ver_error)s</span>
                        <br>
                    </td>
                </tr>
                <tr>
                    <td><label for="email">Email (optional)</label></td>
                    <td>
                        <input name="email" value="%(email)s"/>
                        <span class="error">%(email_error)s</span>
                        <br>
                    </td>
                </tr>
            </tbody>
            <br>
            <input type="submit"/>
        </form>

</body></html>"""
    #  type='email' will pop screen with error not error msg
    # submit = "<input type='submit' value='Submit'/>"
    # form = ("<form method='post'>" +
    #         rotate_label + rotation_input + "<br>" +
    #         message_label + textarea + "<br>" +
    #         submit + "</form>")
    #
    # header = "<h2> Web Caesar</h2>"
    #content = Username
    return form

USER_RE = re.compile("^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile("^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile("^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return not email or EMAIL_RE.match(email)
#in post handler
#def post (self):


class BaseHandler(webapp2.RequestHandler):
        # uses the variables from above to initialize form what is in quotes is what is in "form"
        #afrer the : is what we are passing out
    def write_form(self, pw_error="",ver_error="",user_error="",email_error="",
                username="",email=""):

        self.response.out.write(build_page() % {"pw_error": cgi.escape(pw_error),
                                            "ver_error": cgi.escape(ver_error),
                                            "user_error": cgi.escape(user_error),
                                            "email_error": cgi.escape(email_error),
                                            "username": cgi.escape(username),
                                            "email": cgi.escape(email)})

    def get(self):

        self.write_form()

    def post(self):
        have_error= False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        # username = valid_name(username)
        # password = valid_pwd(password)
        # email = valid_email(email)
        content = dict(username=username,email=email
                        )

        if not valid_username(username):
            content ['user_error'] = "That's not a valid username."
            have_error = True

        if not valid_password(password):
            content ['pw_error'] = "That's not a valid Password"
            have_error = True

        elif password != verify:
            content ['ver_error'] = "Your Password didn't match"
            have_error = True

        if not valid_email(email):
            content ['email_error']= "Thats not a valid email"
            have_error = True

        if have_error:
            self.write_form(**content)
        else:
            self.redirect('/welcome?username=%s' % username)


class WelcomeHandler(webapp2.RequestHandler):
    def get(self):

        username=self.request.get('username')

        if valid_username(username):
            self.response.out.write("<b>WELCOME " + username + " !</b>")
            # self.render("Welcome " + username + "!")
        else:
            self.redirect('/')


app = webapp2.WSGIApplication([
    ('/', BaseHandler),
    ('/welcome', WelcomeHandler),

], debug=True)
