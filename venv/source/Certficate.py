# -*- coding: utf-8 -*-
# define functions for Class Certificate
# By yanxing
from OpenSSL import crypto
import time
import pyasn1


class Certficate:
    def __init__(self):
        self._X509Cert = crypto.X509()
        self._pk = crypto.PKey()
        return

    '''
    导入证书: 从外部文件中导入证书，以及对应的密钥
    pcertfile: 证书文件名，为ASN1编码的证书文件
    pkeyfile: 密钥文件名，为PEM编码的密钥数据
    '''
    def loadcert(self, pcertfile, pkeyfile):
        file = open(pcertfile, "rb")
        buf = file.read()
        self._X509Cert = crypto.load_certificate(crypto.FILETYPE_ASN1, buf)
        file.close()
        file = open(pkeyfile, "rb")
        buf = file.read()
        file.close()
        self._pk = crypto.load_privatekey(crypto.FILETYPE_PEM, buf)
        return

    '''
    生成证书: 创建一个证书对象，设置相关的属性值，可用另一个证书来签发，生成实际的证书
    pattrlist: 属性列表，字典方式
    '''
    def createcert(self, pattrlist):
        # create s cert object
        self._X509Cert = crypto.X509()
        # set public Key
        self._pk = crypto.PKey()
        self._pk.generate_key(crypto.TYPE_RSA, 1024)
        self._X509Cert.set_pubkey(self._pk)
        # set Subject
        cn_name = pattrlist["cn"]
        subject = self._X509Cert.get_subject()
        setattr(subject, 'C', 'CN')
        setattr(subject, "CN", cn_name)
        # set validity
        self._X509Cert.gmtime_adj_notBefore(0)
        self._X509Cert.gmtime_adj_notAfter(60)
        notafter = pattrlist["notAfter"]
        self._X509Cert.set_notAfter(notafter)
        notbefore = pattrlist["notBefore"]
        self._X509Cert.set_notBefore(notbefore)
        # set Serial
        self._X509Cert.set_serial_number(pattrlist["serial_num"])
        return

    '''
    签发证书: 签发证书
    pcert: 证书对象
    '''
    def signcert(self, pcert):
        # set issuer
        pcert._X509Cert.set_issuer(self._X509Cert.get_subject())
        # sign Cert
        pcert._X509Cert.sign(self._pk, "sha256")
        return

    '''
    导出证书: 导出证书与密钥到相应的文件
    keyfile: 密钥文件名
    certfile：证书文件名
    '''
    def dumpcert(self, keyfile, certfile):
        buf = crypto.dump_privatekey(crypto.FILETYPE_PEM, self._pk)
        keyfile = open(keyfile, "wb")
        keyfile.write(buf)
        keyfile.close()
        dumpcert = crypto.dump_certificate(crypto.FILETYPE_ASN1, self._X509Cert)
        certfile = open(certfile, "wb")
        certfile.write(dumpcert)
        certfile.close()
        return
