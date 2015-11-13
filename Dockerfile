FROM abstracttechnology/plone:4.3
MAINTAINER Giorgio Borelli <giorgio@giorgioborelli.it>

USER root

# Update buildout.cfg add colorpicker source and run the buildout
COPY docker-buildout.cfg buildout.cfg
COPY . src/collective.z3cform.mapwidget

RUN chown -R webapp:webapp src buildout.cfg

USER webapp
RUN python bin/buildout -v
