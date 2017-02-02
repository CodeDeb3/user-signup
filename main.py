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
                        <input name="username" type="text" value="%(username)s" required="">
                        <span class="error">That's not a valid username</span>
                        <div style = "color: red">%(error)s<div>

                        <br>
                    </td>
                </tr>
                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" type="password" value="" required="">
                        <span class="error">That's not a valid password</span>
                        <div style = "color: red">%(error)s<div>
                        <br>
                    </td>
                </tr>
                <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify" type="password" required="">
                        <span class="error">Passwords don't match</span>
                        <br>
                    </td>
                </tr>
                <tr>
                    <td><label for="email">Email (optional)</label></td>
                    <td>
                        <input name="email" type="email" value="">
                        <span class="error">That's not a valid email</span>
                        <br>
                    </td>
                </tr>
            </tbody>
            <input type="submit">
        </form>

</body></html>"""
        # error = self.request.get("error")
        # if error:
        #     error_element = ("<p class='error'>" + cgi.escape (error, quote=True) + "</p>")
        # else:
        #     error_element=""

    #Username = "<label>username </label>"
    # name_input = "<input type ='number' name='rotation'/>"
    #
    # message_label = "<label class='blah'> Type a message: </label>"
    # textarea = "<textarea name='message'>" + textarea_content + "</textarea>"
    #
    # submit = "<input type='submit' value='Submit'/>"
    # form = ("<form method='post'>" +
    #         rotate_label + rotation_input + "<br>" +
    #         message_label + textarea + "<br>" +
    #         submit + "</form>")
    #
    # header = "<h2> Web Caesar</h2>"
    #content = Username
    return form
#USER_RE = re.compile

class MainHandler(webapp2.RequestHandler):
    def write_form(self,error="",username="",password=""):
        self.response.out.write(form % {"error": error,
                                        "username": escape_html(username),
                                        "password": escape_html(password),
                                        "validate": escape_html(validate),
                                        #"email": escape_html(email)})                                       )
    def get(self):

        self.response.out.write(build_page)

    def post (self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        username = valid_name(username)
        password = valid_pwd(password)
        email = valid_email(email)

        if not (username and password):
            self.write.form ('error try again'), username,email
        else:
            self.redirect("/Welcome")

#         #q = self.request.get("q")
#         #self.response.out.write(q)
#
#         self.response.headers['Content-Type']='text/plain'

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
#         username = self.request.get('username')
        if username== (username):
            self.response.out.write("Welcome " + username + "!")
        else:
            self.redirect('/')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Welcome', WelcomeHandler),

], debug=True)
