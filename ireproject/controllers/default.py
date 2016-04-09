# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    redirect(URL("default", "search"))
    return dict(message=T('Welcome to web2py!'))

def search():
    form = FORM(INPUT(_type="text", _name="search"),
                INPUT(_type="submit", _value="Search"),
                _action="",
                _method="GET",
                _class="col offset-s3 s6")

    table = TABLE()

    if request.get_vars != {}:
        ptable = db.product
        q = request.get_vars["search"]
	query = (ptable.name.contains(q))
	query &= (ptable.price != "")
        rows = db(query).select()
        table = TABLE(_class="centered striped")
        table.append(TR(TH("Product ID"),
                        TH("Image"),
                        TH("Name"),
                        TH("Ratings"),
                        TH("Price"),
                        TH("OS"),
                        TH("Colour"),
                        TH("More")))
        for row in rows:
            tr = TR()
            append = tr.append
            append(TD(row.product_id))
            append(TD(A(IMG(_src=URL("static",
                                     "images/products/product_" + str(row.product_id) + ".jpg")),
                        _href=URL("default",
                                  "product_details",
                                  args=row.product_id))))
            append(TD(row.name))
            append(TD(row.ratings))
            append(TD(row.price))
            append(TD(row.os))
            append(TD(row.colour))
            #append(TD(row.colour))
            table.append(tr)

    return dict(form=form,
                table=table)

def product_details():
    if request.args == []:
        session.flash = "Click on an image"
        redirect(URL("default", "search"))

    ptable = db.product
    product_id = int(request.args[0])
    record = db(ptable.product_id == product_id).select().first()
    table = TABLE(_class="centered")
    tr = TR()
    tr.append(TD(IMG(_src=URL("static",
                              "images/products/product_" + \
                              str(product_id) + ".jpg"))))
    tr.append(TD(TABLE(TR(TD("Name:"),
                          TD(record.name)),
                       TR(TD("Price:"),
                          TD(record.price)),
                       TR(TD("Rating:"),
                          TD(record.ratings)),
                       TR(TD("OS:"),
                          TD(record.os)),
                       TR(TD("Colour:"),
                          TD(record.colour)),
                       TR(TD("RAM:"),
                          TD(record.ram)),
                       TR(TD("Dimensions:"),
                          TD(record.product_dimensions)),
                       TR(TD("Connectivity:"),
                          TD(record.connectivity_technologies)),
                       TR(TD("Special Features:"),
                          TD(record.special_features)),
                       TR(TD("Date:"),
                          TD(record.date_now)),
                       _class="centered striped")))
    table.append(tr)
    return dict(table=table)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


