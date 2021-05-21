// 인증이 필요한 컴포넌트를 위한 전용 라우트

import React from 'react';
import { Route, Redirect } from 'react-router-dom';

const AuthRoute = ({
  authenticated,
  component: Component,
  render,
  ...rest
}) => {
  return (
    <Route
      {...rest}
      render={(props) =>
        authenticated ? (
          render ? (
            render(props)
          ) : (
            <Component {...props} />
          )
        ) : (
          <Redirect
            to={{ pathname: '/login', state: { from: props.location } }}
          />
          // state 옵션에 현재 location을 그대로 넘겨줌, 로그인 후에 다시 이 페이지로 돌아오게하기위함!
        )
      }
    />
  );
};

export default AuthRoute;
