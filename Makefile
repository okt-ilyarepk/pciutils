# Makefile for source rpm: pciutils
# $Id$
NAME := pciutils
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
