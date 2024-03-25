# coding: utf-8

"""
    GroupDocs.Translation SDK

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 24.3.0
    Contact: anton.perhunov@aspose.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class HttpStatusCode(int, Enum):
    """
    HttpStatusCode
    """

    """
    allowed enum values
    """
    NUMBER_100 = 100
    NUMBER_101 = 101
    NUMBER_102 = 102
    NUMBER_103 = 103
    NUMBER_200 = 200
    NUMBER_201 = 201
    NUMBER_202 = 202
    NUMBER_203 = 203
    NUMBER_204 = 204
    NUMBER_205 = 205
    NUMBER_206 = 206
    NUMBER_207 = 207
    NUMBER_208 = 208
    NUMBER_226 = 226
    NUMBER_300 = 300
    NUMBER_301 = 301
    NUMBER_302 = 302
    NUMBER_303 = 303
    NUMBER_304 = 304
    NUMBER_305 = 305
    NUMBER_306 = 306
    NUMBER_307 = 307
    NUMBER_308 = 308
    NUMBER_400 = 400
    NUMBER_401 = 401
    NUMBER_402 = 402
    NUMBER_403 = 403
    NUMBER_404 = 404
    NUMBER_405 = 405
    NUMBER_406 = 406
    NUMBER_407 = 407
    NUMBER_408 = 408
    NUMBER_409 = 409
    NUMBER_410 = 410
    NUMBER_411 = 411
    NUMBER_412 = 412
    NUMBER_413 = 413
    NUMBER_414 = 414
    NUMBER_415 = 415
    NUMBER_416 = 416
    NUMBER_417 = 417
    NUMBER_421 = 421
    NUMBER_422 = 422
    NUMBER_423 = 423
    NUMBER_424 = 424
    NUMBER_426 = 426
    NUMBER_428 = 428
    NUMBER_429 = 429
    NUMBER_431 = 431
    NUMBER_451 = 451
    NUMBER_500 = 500
    NUMBER_501 = 501
    NUMBER_502 = 502
    NUMBER_503 = 503
    NUMBER_504 = 504
    NUMBER_505 = 505
    NUMBER_506 = 506
    NUMBER_507 = 507
    NUMBER_508 = 508
    NUMBER_510 = 510
    NUMBER_511 = 511

    @classmethod
    def from_json(cls, json_str: str) -> HttpStatusCode:
        """Create an instance of HttpStatusCode from a JSON string"""
        return HttpStatusCode(json.loads(json_str))


